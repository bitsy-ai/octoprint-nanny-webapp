# Generated by Django 3.2.2 on 2021-05-30 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telemetry', '0010_auto_20210530_1132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telemetryevent',
            old_name='created_dt',
            new_name='ts',
        ),
        migrations.RemoveField(
            model_name='telemetryevent',
            name='octoprint_version',
        ),
    ]
