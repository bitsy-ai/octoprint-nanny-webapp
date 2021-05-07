from enum import Enum
from typing import Union, Optional
from django.apps import apps
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.conf import settings
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

OctoPrintDevice = apps.get_model("remote_control", "OctoPrintDevice")
AlertMessage = apps.get_model("alerts", "AlertMessage")
GeeksToken = apps.get_model("partners", "GeeksToken")
User = get_user_model()
##
# Serializers for use with third-party partners and external systems
# These serializers exclude personally-identifying info
##


class PartnersEnum(Enum):
    """
    Used to determine if print_nanny_webapp.alerts.Alert.AlertMethodChoices is internal or external
    External partners receive a more limited set of data, with PII and other sensitive info excluded from serializers
    """

    PARTNER_3DGEEKS = "PARTNER_3DGEEKS"


class PartnerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "")


class Partner3DGeeksMetadataSerializer(serializers.ModelSerializer):
    """
    Please do not include any personally-identifying info or sensitive info in partner serializers
    """

    verified = serializers.SerializerMethodField()

    def get_verified(self, obj):
        return obj.geekstoken_set.first().verified

    print_nanny_plugin_version = serializers.SerializerMethodField()

    def get_print_nanny_plugin_version(self, obj):
        return obj.plugin_version

    class Meta:
        model = OctoPrintDevice
        fields = (
            "name",
            "model",
            "platform",
            "octoprint_version",
            "print_nanny_plugin_version",
            "print_nanny_client_version",
            "verified",
        )


class Partner3DGeeksAlertSerializer(serializers.ModelSerializer):
    """
        Do not use underscores in this serializer - linitation of Firebase Cloud Messaging
    """

    timeLeft = serializers.SerializerMethodField(method_name='get_time_left')

    def get_time_left(self, obj) -> int:
        if obj.print_session:
            return obj.print_session.time_remaining
        return 0

    currentTime = serializers.SerializerMethodField(method_name='get_current_time')

    def get_current_time(self, obj) -> int:
        if obj.print_session:
            return obj.print_session.current_time
        return 0

    event = serializers.SerializerMethodField()

    def get_event(self, obj) -> str:
        return obj.event_type

    printer = serializers.SerializerMethodField()

    def get_printer(self, obj) -> str:
        return obj.octoprint_device.name

    print = serializers.SerializerMethodField()

    def get_print(self, obj) -> str:
        if obj.print_session:
            return obj.print_session.gcode_file
        return str()

    percent = serializers.SerializerMethodField()

    def get_percent(self, obj) -> int:
        if obj.print_session:
            return obj.print_session.progress
        return 0

    token = serializers.SerializerMethodField()

    def get_token(self, obj) -> str:
        print(obj.__dict__)
        token = GeeksToken.objects.get(octoprint_device_id=obj.octoprint_device.id)
        return token.key.hex

    action = serializers.SerializerMethodField()

    def get_action(self, obj) -> str:
        device_url = reverse(
            "dashboard:octoprint-devices:detail",
            kwargs={"pk": obj.octoprint_device.id},
        )
        device_url = urljoin(settings.BASE_URL, device_url)
        return device_url

    image = serializers.SerializerMethodField()

    def get_image(self, obj) -> Optional[str]:
        return None

    class Meta:
        model = AlertMessage
        fields = (
            "event",
            "token",
            "printer",
            "print",
            "currentTime",
            "timeLeft",
            "percent",
            "image",
            "action",
        )
