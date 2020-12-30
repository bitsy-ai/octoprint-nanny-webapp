# Generated by Django 3.1.3 on 2020-12-30 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("client_events", "0009_auto_20201228_1434"),
        ("remote_control", "0005_auto_20201227_1910"),
    ]

    operations = [
        migrations.AddField(
            model_name="printjob",
            name="octoprint_device",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="client_events.octoprintdevice",
            ),
        ),
    ]
