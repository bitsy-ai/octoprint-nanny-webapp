from typing import Optional

from django.apps import apps
from print_nanny_webapp.alerts.api.serializer import AlertSerializer
from print_nanny_webapp.partners.api.serializer import (
    PartnerAlertSerializer,
    PartnersEnum,
)
from django.conf import settings

from print_nanny_webapp.models.alerts import AlertEventTypes
AlertMessage = apps.get_model("alerts", "AlertMessage")
GeeksToken = apps.get_model("partners", "GeeksToken")

class AlertTask:
    """
    Serializes Alert instance to JSON payload
    Triggers various alert methods with payload data
    """

    def __init__(
            self, 
            instance: AlertMessage, 
            email_body_txt_template: str="email/generic_alert_body.txt", 
            email_body_html_template: Optional[str]=None,
            email_subject_template: str="email/generic_alert_subject.txt",
            serializer=AlertSerializer,
            partner_serializer=PartnerAlertSerializer
        ):
        self.instance = instance
        self.email_body_txt_template = email_body_txt_template
        self.email_body_html_template = email_body_html_template
        self.email_subject_template = email_subject_template
        self.serializer = serializer
        self.partner_serializer = partner_serializer
        self.alert_trigger_method_map = {
            AlertModel.AlertMethodChoices.UI: self.trigger_ui_alert,
            AlertModel.AlertMethodChoices.EMAIL: self.trigger_email_alert,
            AlertModel.AlertMethodChoices.DISCORD: self.trigger_discord_alert,
            AlertModel.AlertMethodChoices.GEEKS3D: self.trigger_geeks3d_alert,
        }

    def trigger_alert(self) -> bool:
        """
        Returns a bool expressing whether method call resulted in alert being triggered
        Duplicate alert triggers will be ignored
        """
        if self.sent is False:
            self.alert_trigger_method_map[alert_method]()
            self.sent = True
            self.save()
            return True
        return False

    def get_serializer(self) -> Union[AlertSerializer, PartnerAlertSerializer]:
        if self.instance.alert_method.value in PartnersEnum:
            return self.partner_serializer(self.instance)
        return self.serializer(self.instance)
    
    def trigger_geeks3d_alert(self):
        serializer = self.get_serializer()
        data = serializer.data
        data['token'] = GeeksToken.get(octoprint_device_id=self.instance.octoprint_device_id)
        return requests.post(settings.PARTNERS_3DGEEKS_SETTINGS['alerts_push'], json=data)

    def trigger_ui_alert(self):
        serializer = self.get_serializer()
        data = serializer.data

        channel_layer = get_channel_layer()

        # vuex namespace
        data["namespace"] = "alerts_dropdown"
        # required by websocket message handler in vue app(s)
        data["action"] = "alertMessage"

        async_to_sync(channel_layer.group_send)(
            f"alerts_{self.user.id}",
            {
                "type": "alert.message",
                # https://github.com/nathantsoi/vue-native-websocket#with-format-json-enabled
                "data": JSONRenderer().render(data),
            },
        )

    def trigger_email_alert(self):

        device_url = reverse(
            "dashboard:octoprint-devices:detail",
            kwargs={"pk": self.instance.octoprint_device.id},
        )
        merge_data = {
            "DEVICE_URL": device_url,
            "FIRST_NAME": self.instance.user.first_name or "Maker",
            "DEVICE_NAME": self.instance.octoprint_device.name,
        }
        if self.event_type is AlertEventTypes.VIDEO_DONE:
            videos_url = reverse(
                "dashboard:videos:list"
            )
            merge_data.update({"VIDEO_DASHBOARD_URL": videos_url })

        elif self.event_type is AlertEventTypes.PRINT_PROGRESS and self.instance.print_session:
            merge_data.update({"PRINT_PROGRESS": self.instance.print_session.print_progress })

        text_body = render_to_string(self.instance.email_body_txt_template, merge_data)
        subject = render_to_string(self.instance.email_subject_template, merge_data)
        message = AnymailMessage(
            subject=subject,
            body=text_body,
            to=[self.instance.user.email],
            tags=[
                self.__class__,
                f"User:{self.instance.user.id}",
                f"Device:{self.instance.octoprint_device.id}",
                f"PrintSessionID:{self.instance.print_session.id}",
                f"PrintSession:{self.instance.print_session.session}",
            ],
        )
        message.send()
        return message

    def trigger_discord_alert(self):
        raise NotImplementedError

