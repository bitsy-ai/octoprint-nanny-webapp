# Generated by Django 3.1.7 on 2021-05-10 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remotecontrolcommand",
            name="command",
            field=models.CharField(
                choices=[
                    ("monitoring_stop", "Stop Print Nanny Monitoring"),
                    ("monitoring_start", "Start Print Nanny Monitoring"),
                    ("print_start", "Start Print"),
                    ("print_stop", "Stop Print"),
                    ("print_pause", "Pause Print"),
                    ("print_resume", "Resume Print"),
                    ("move_nozzle", "Move Nozzle"),
                    ("ping", "Ping"),
                ],
                max_length=255,
            ),
        ),
    ]