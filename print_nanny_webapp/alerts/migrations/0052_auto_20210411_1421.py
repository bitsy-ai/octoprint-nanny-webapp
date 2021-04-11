# Generated by Django 3.1.7 on 2021-04-11 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0051_remove_remotecontrolcommandalertsettings_snapshot"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="alert",
            name="dismissed",
        ),
        migrations.AddField(
            model_name="printsessionalertsettings",
            name="needs_review",
            field=models.BooleanField(default=False),
        ),
    ]
