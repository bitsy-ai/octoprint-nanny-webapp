# Generated by Django 3.2.2 on 2021-06-22 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0018_alter_printsession_created_dt"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="octoprintdevice",
            name="monitoring_active",
        ),
        migrations.RemoveField(
            model_name="octoprintdevice",
            name="monitoring_mode",
        ),
        migrations.RemoveField(
            model_name="octoprintdevice",
            name="print_job_status",
        ),
        migrations.AddField(
            model_name="printsession",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="printsession",
            name="octoprint_device",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="print_sessions",
                to="remote_control.octoprintdevice",
            ),
        ),
    ]