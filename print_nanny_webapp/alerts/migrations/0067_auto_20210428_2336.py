# Generated by Django 3.1.7 on 2021-04-29 06:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models
import print_nanny_webapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("remote_control", "0043_auto_20210428_1513"),
        ("alerts", "0066_printprogresseventsettings_squashed_0077_auto_20210427_2315"),
    ]

    operations = [
        migrations.CreateModel(
            name="AlertMessage",
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
                (
                    "alert_method",
                    models.CharField(
                        choices=[
                            ("UI", "Print Nanny UI"),
                            ("EMAIL", "Email notifications"),
                            ("DISCORD", "Discord channel (webhook)"),
                            ("PARTNER_3DGEEKS", "3D Geeks mobile app"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("VideoDone", "VideoDone"),
                            ("PrintHealth", "PrintHealth"),
                            ("PrintProgress", "PrintProgress"),
                            ("PrintDone", "PrintDone"),
                            ("PrintFailed", "PrintFailed"),
                            ("PrintPaused", "PrintPaused"),
                            ("PrintResumed", "PrintResumed"),
                            ("PrintStarted", "PrintStarted"),
                        ],
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "annotated_video",
                    models.FileField(
                        null=True, upload_to=print_nanny_webapp.alerts.models._upload_to
                    ),
                ),
                ("created_dt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_dt", models.DateTimeField(auto_now=True, db_index=True)),
                ("seen", models.BooleanField(default=False)),
                ("sent", models.BooleanField(default=False)),
                (
                    "octoprint_device",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.octoprintdevice",
                    ),
                ),
                (
                    "print_session",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="remote_control.printsession",
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
        migrations.CreateModel(
            name="AlertSettings",
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
                ("created_dt", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_dt", models.DateTimeField(auto_now=True, db_index=True)),
                (
                    "alert_methods",
                    print_nanny_webapp.utils.fields.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("UI", "Print Nanny UI"),
                                ("EMAIL", "Email notifications"),
                                ("DISCORD", "Discord channel (webhook)"),
                                ("PARTNER_3DGEEKS", "3D Geeks mobile app"),
                            ],
                            max_length=255,
                        ),
                        blank=True,
                        default=("EMAIL",),
                        size=None,
                    ),
                ),
                (
                    "event_types",
                    print_nanny_webapp.utils.fields.ChoiceArrayField(
                        base_field=models.CharField(
                            choices=[
                                ("PrintHealth", "Print health alerts"),
                                (
                                    "PrintStatus",
                                    "Print status updates (started, percent progress, paused, resumed, cancelling, cancelled, failed, done)",
                                ),
                            ],
                            max_length=255,
                        ),
                        blank=True,
                        default=("PrintHealth", "PrintStatus"),
                        size=None,
                    ),
                ),
                (
                    "discord_webhook",
                    models.CharField(
                        blank=True,
                        help_text="Send notifications to a Discord channel. Please check out this guide to <a href='https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks'>generate a webhook</a> url and paste it here.",
                        max_length=255,
                        null=True,
                    ),
                ),
                (
                    "print_progress_percent",
                    models.IntegerField(
                        default=25,
                        help_text="Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="alerteventsettings",
            name="user",
        ),
        migrations.RemoveField(
            model_name="alertplot",
            name="alert",
        ),
        migrations.RemoveField(
            model_name="manualvideouploadalert",
            name="alert_ptr",
        ),
        migrations.RemoveField(
            model_name="printsessionalert",
            name="alert_ptr",
        ),
        migrations.RemoveField(
            model_name="printsessionalert",
            name="print_session",
        ),
        migrations.DeleteModel(
            name="Alert",
        ),
        migrations.DeleteModel(
            name="AlertEventSettings",
        ),
        migrations.DeleteModel(
            name="AlertPlot",
        ),
        migrations.DeleteModel(
            name="ManualVideoUploadAlert",
        ),
        migrations.DeleteModel(
            name="PrintSessionAlert",
        ),
    ]