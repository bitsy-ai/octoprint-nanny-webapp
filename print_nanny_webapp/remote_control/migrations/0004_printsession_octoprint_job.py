# Generated by Django 3.2.2 on 2021-05-11 07:00

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0003_auto_20210510_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='printsession',
            name='octoprint_job',
            field=django.contrib.postgres.fields.jsonb.JSONField(null=True),
        ),
    ]
