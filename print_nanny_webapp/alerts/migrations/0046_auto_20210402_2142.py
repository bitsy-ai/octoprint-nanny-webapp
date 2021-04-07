# Generated by Django 3.1.7 on 2021-04-03 04:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("contenttypes", "0002_remove_content_type_name"),
        ("remote_control", "0053_printsession_supress_alerts"),
        ("alerts", "0045_auto_20210402_2140"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="PrintSessionAlertAlert",
            new_name="PrintSessionAlert",
        ),
        migrations.RenameModel(
            old_name="PrintSessionAlertAlertSettings",
            new_name="PrintSessionAlertSettings",
        ),
    ]