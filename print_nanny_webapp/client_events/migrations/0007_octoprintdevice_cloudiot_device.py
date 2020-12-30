# Generated by Django 3.1.3 on 2020-12-28 06:53

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("client_events", "0006_octoprintdevice_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="octoprintdevice",
            name="cloudiot_device",
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
