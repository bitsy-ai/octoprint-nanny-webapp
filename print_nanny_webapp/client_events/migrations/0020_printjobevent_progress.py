# Generated by Django 3.1.3 on 2021-01-18 23:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("client_events", "0019_remove_printjobevent_progress"),
    ]

    operations = [
        migrations.AddField(
            model_name="printjobevent",
            name="progress",
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]
