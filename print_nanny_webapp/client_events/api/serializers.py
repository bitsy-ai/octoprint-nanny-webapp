from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from print_nanny_webapp.client_events.models import (
    ClientEvent,
    OctoPrintEvent,
    PrintJobState,
    PluginEvent,
)


class ClientEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientEvent
        fields = [field.name for field in ClientEvent._meta.fields] + ["url"]

        read_only_fields = ("user",)


class OctoPrintEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = OctoPrintEvent
        fields = [field.name for field in OctoPrintEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:octoprint-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)


class PluginEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PluginEvent
        fields = [field.name for field in PluginEvent._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:plugin-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)


class PrintJobStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrintJobState
        fields = [field.name for field in PrintJobState._meta.fields] + ["url"]
        extra_kwargs = {
            "url": {"view_name": "api:print-job-event-detail", "lookup_field": "id"}
        }
        read_only_fields = ("user",)


class ClientEventPolymorphicSerializer(PolymorphicSerializer):
    resource_type_field_name = "type"

    model_serializer_mapping = {
        ClientEvent: ClientEventSerializer,
        PrintJobState: PrintJobStateSerializer,
        OctoPrintEvent: OctoPrintEventSerializer,
        PluginEvent: PluginEventSerializer,
    }

    def to_resource_type(self, model_or_instance):
        return model_or_instance._meta.object_name.lower()
