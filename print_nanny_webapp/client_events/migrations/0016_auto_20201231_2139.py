# Generated by Django 3.1.3 on 2021-01-01 05:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0008_octoprintdevice_cloudiot_device_name"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("client_events", "0015_auto_20201231_1936"),
    ]

    operations = [
        migrations.RenameField(
            model_name="octoprintevent",
            old_name="dt",
            new_name="created_dt",
        ),
        migrations.RemoveField(
            model_name="octoprintevent",
            name="print_job",
        ),
        migrations.AlterField(
            model_name="octoprintevent",
            name="event_type",
            field=models.CharField(
                choices=[
                    ("ClientAuthed", "ClientAuthed"),
                    ("ClientClosed", "ClientClosed"),
                    ("ClientDeauthed", "ClientDeauthed"),
                    ("ClientOpened", "ClientOpened"),
                    ("SettingsUpdated", "SettingsUpdated"),
                    ("UserLoggedIn", "User Logged In"),
                    ("UserLoggedOut", "User Logged Out"),
                    ("FileAdded", "FileAdded"),
                    ("FileRemoved", "FileRemoved"),
                    ("FolderAdded", "FolderAdded"),
                    ("FolderRemoved", "FolderRemoved"),
                    ("TransferDone", "TransferDone"),
                    ("TransferFailed", "TransferFailed"),
                    ("TransferStarted", "TransferStarted"),
                    ("UpdatedFiles", "UpdatedFiles"),
                    ("Upload", "Upload"),
                    ("CaptureDone", "CaptureDone"),
                    ("CaptureFailed", "CaptureFailed"),
                    ("CaptureStart", "CaptureStart"),
                    ("MovieDone", "MovieDone"),
                    ("MovieFailed", "MovieFailed"),
                    ("MovieRendering", "MovieRendering"),
                    ("PostRollEnd", "PostRollEnd"),
                    ("PostRollStart", "PostRollStart"),
                    ("SlicingCancelled", "SlicingCancelled"),
                    ("SlicingDone", "SlicingDone"),
                    ("SlicingFailed", "SlicingFailed"),
                    ("SlicingProfileAdded", "SlicingProfileAdded"),
                    ("SlicingProfileDeleted", "SlicingProfileDeleted"),
                    ("SlicingProfileModified", "SlicingProfileModified"),
                    ("SlicingStarted", "SlicingStarted"),
                    ("Connected", "Connected"),
                    ("Disconnected", "Disconnected"),
                    ("PrinterReset", "PrinterReset"),
                    ("PrinterStateChanged", "PrinterStateChanged"),
                    ("FirmwareData", "FirmwareData"),
                    ("PrinterProfileAdded", "PrinterProfileAdded"),
                    ("PrinterProfileDeleted", "PrinterProfileDeleted"),
                    ("PrinterProfileModified", "PrinterProfileModified"),
                    ("PrintProgress", "PrintProgress"),
                    (
                        "plugin_pi_support_throttle_state",
                        "plugin_pi_support_throttle_state",
                    ),
                    ("Shutdown", "Shutdown"),
                    ("Startup", "Startup"),
                ],
                db_index=True,
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="octoprintevent",
            name="octoprint_version",
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name="octoprintevent",
            name="plugin_version",
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name="octoprintevent",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="PrintJobEvent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_dt", models.DateTimeField(db_index=True)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("Error", "Error"),
                            ("PrintCancelled", "PrintCancelled"),
                            ("PrintCancelling", "PrintCancelling"),
                            ("PrintDone", "PrintDone"),
                            ("PrintFailed", "PrintFailed"),
                            ("PrintPaused", "PrintPaused"),
                            ("PrintResumed", "PrintResumed"),
                            ("PrintStarted", "PrintStarted"),
                        ],
                        db_index=True,
                        max_length=255,
                    ),
                ),
                ("current_z", models.FloatField()),
                ("progress", models.FloatField()),
                ("job_data_file", models.CharField(max_length=255)),
                ("event_data", models.JSONField()),
                ("plugin_version", models.CharField(max_length=60)),
                ("octoprint_version", models.CharField(max_length=60)),
                (
                    "print_job",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printjob",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]