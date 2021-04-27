# Generated by Django 3.1.7 on 2021-04-27 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0056_auto_20210427_1242"),
    ]

    operations = [
        migrations.AddField(
            model_name="alert",
            name="alert_method",
            field=models.CharField(
                choices=[
                    ("UI", "Receive Print Nanny UI notifications"),
                    ("EMAIL", "Receive email notifications"),
                    ("DISCORD", "Receive notifications through Discord"),
                    ("PARTNER_3DGEEKS", "Receive notifications in 3D Geeks mobile app"),
                ],
                default="EMAIL",
                max_length=255,
            ),
        ),
    ]