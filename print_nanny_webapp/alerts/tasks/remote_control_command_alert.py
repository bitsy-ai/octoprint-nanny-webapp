
import logging
from django.apps import apps
from celery import group, shared_task, chain
from django.contrib.auth import get_user_model

User = get_user_model()
RemoteControlCommand = apps.get_model('remote_control', 'RemoteControlCommand')
RemoteControlCommandAlert = apps.get_model('alerts', 'RemoteControlCommandAlert')
RemoteControlCommandAlertSettings = apps.get_model('alerts', 'RemoteControlCommandAlertSettings')

logger = logging.getLogger(__name__)
@shared_task
def create_remote_control_command_alerts(user_id, command_id, alert_subtype):


    user = User.objects.get(id=user_id)
    command = RemoteControlCommand(id=command_id)

    alert_settings = RemoteControlCommandAlertSettings(user=user)
    alert_settings_attr = alert_settings.command_to_attr(command.command)

    created_alerts = []
    logging.info(f'Checking alert_subtype={alert_subtype} in {alert_settings_attr}')
    if alert_subtype in alert_settings_attr:
        for alert_method in alert_settings.alert_methods:
            instance = RemoteControlCommandAlert.create(
                alert_method=alert_method,
                user=user,
                command=command,
                alert_subtype=alert_subtype
            )
            logging.info(f'Created alert instance id={instance.id} alert_method={alert_method}')
            instance.trigger_alert()
            created_alerts.append(instance)
        
    return [alert.id for alert in created_alerts]



