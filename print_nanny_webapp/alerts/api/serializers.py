import logging
import inspect

from django.apps import apps
from django.urls import reverse
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from rest_polymorphic.serializers import PolymorphicSerializer

from ..models import (
    ManualVideoUploadAlert,
    RemoteControlCommandAlert,
    Alert,
    ProgressAlert,
    DefectAlert,
    AlertSettings,
    ProgressAlertSettings,
    RemoteControlCommandAlertSettings,
    DefectAlertSettings,
    PrintSessionAlert,
)

logger = logging.getLogger(__name__)

RemoteControlCommand = apps.get_model("remote_control", "RemoteControlCommand")


class AlertSerializer(serializers.ModelSerializer):

    time = serializers.SerializerMethodField()

    def get_time(self, obj):
        return naturaltime(obj.updated_dt)

    class Meta:
        model = Alert
        fields = ["created_dt", "updated_dt", "user", "dismissed", "time"]
        read_only_fields = ("user",)


class ProgressAlertSerializer(AlertSerializer):
    class Meta:
        model = ProgressAlert
        fields = "__all__"
        read_only_fields = ("user", "alert_methods", "alert_type", "polymorphic_ctype")


class CreateDefectAlertSerializer(AlertSerializer):
    print_session = serializers.CharField()

    class Meta:
        model = DefectAlert
        fields = ("print_session",)


class CreatePrintSessionAlertSerializer(AlertSerializer):
    print_session = serializers.CharField()

    class Meta:
        model = PrintSessionAlert
        fields = ("print_session",)


class PrintSessionAlertSerializer(AlertSerializer):
    class Meta:
        model = DefectAlert
        fields = [
            "id",
            "time",
            "alert_methods",
            "alert_type",
            "created_dt",
            "updated_dt",
            "seen",
            "dismissed",
            "user",
            "octoprint_device",
            "print_session",
        ]

        read_only_fields = (
            "alert_methods",
            "alert_type",
            "polymorphic_ctype",
            "user",
            "octoprint_device",
        )


class DefectAlertSerializer(AlertSerializer):
    supress_url = serializers.HyperlinkedIdentityField(
        view_name="api:defect-alert-supress", lookup_field="pk"
    )
    supress_url = serializers.HyperlinkedIdentityField(
        view_name="api:defect-alert-stop-print", lookup_field="pk"
    )

    class Meta:
        model = DefectAlert
        fields = [
            "id",
            "time",
            "alert_methods",
            "alert_type",
            "created_dt",
            "updated_dt",
            "seen",
            "dismissed",
            "user",
            "octoprint_device",
            "print_session",
            "supress_url",
        ]

        read_only_fields = (
            "alert_methods",
            "alert_type",
            "polymorphic_ctype",
            "user",
            "octoprint_device",
        )


class AlertBulkRequestSerializer(serializers.Serializer):
    """
    Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    """

    ids = serializers.ListField(child=serializers.IntegerField())


class AlertBulkResponseSerializer(serializers.Serializer):
    """
    Serializer used in POST /api/alerts/seen and POST /api/alerts/dismiss requests
    """

    received = serializers.IntegerField()
    updated = serializers.IntegerField()


class RemoteControlCommandAlertSerializer(AlertSerializer):

    dashboard_url = serializers.SerializerMethodField()

    def get_dashboard_url(self, obj):
        return reverse(
            "dashboard:octoprint-devices:detail", kwargs={"pk": obj.command.device.id}
        )

    snapshot_url = serializers.SerializerMethodField()

    def get_snapshot_url(self, obj):
        lastest_snapshot = obj.command.snapshots.order_by("-created_dt").first()
        if lastest_snapshot:
            return lastest_snapshot.image.url

    metadata = serializers.SerializerMethodField()

    def get_metadata(self, obj):
        return obj.command.metadata

    icon = serializers.CharField()
    description = serializers.CharField()
    color = serializers.CharField()
    title = serializers.CharField()

    class Meta:
        model = RemoteControlCommandAlert
        fields = [
            "alert_subtype",
            "alert_methods",
            "alert_type",
            "color",
            "created_dt",
            "dashboard_url",
            "dismissed",
            "metadata",
            "icon",
            "id",
            "time",
            "description",
            "seen",
            "snapshot_url",
            "title",
            "updated_dt",
            "user",
        ]
        read_only_fields = ("user",)


class ManualVideoUploadAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManualVideoUploadAlert
        fields = ["created_dt", "updated_dt", "user", "dismissed", "alert_type"]
        read_only_fields = ("user",)


class AlertPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "type"

    model_serializer_mapping = {
        Alert: AlertSerializer,
        RemoteControlCommandAlert: RemoteControlCommandAlertSerializer,
        ManualVideoUploadAlert: ManualVideoUploadAlertSerializer,
        DefectAlert: DefectAlertSerializer,
        ProgressAlert: ProgressAlertSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class AlertSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class CommandAlertSettingsSerializer(AlertSettingsSerializer):
    class Meta:
        model = RemoteControlCommandAlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class DefectAlertSettingsSerializer(AlertSettingsSerializer):
    class Meta:
        model = DefectAlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class ProgressAlertSettingsSerializer(AlertSettingsSerializer):
    class Meta:
        model = ProgressAlertSettings
        fields = "__all__"
        read_only_fields = ("user",)


class AlertSettingsPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "type"

    model_serializer_mapping = {
        AlertSettings: AlertSettingsSerializer,
        RemoteControlCommandAlertSettings: CommandAlertSettingsSerializer,
        DefectAlertSettings: DefectAlertSettingsSerializer,
        ProgressAlert: ProgressAlertSettingsSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()


class AlertMethodSerializer(serializers.Serializer):

    label = serializers.CharField()
    value = serializers.CharField()
