# Generated by Django 3.1.7 on 2021-04-03 04:40

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("remote_control", "0053_printsession_supress_alerts"),
        ("alerts", "0044_printsessiondonealertsettings"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PrintSessionDoneAlert",
            new_name="PrintSessionAlertAlert",
        ),
        migrations.RenameModel(
            old_name="PrintSessionDoneAlertSettings",
            new_name="PrintSessionAlertAlertSettings",
        ),
    ]
