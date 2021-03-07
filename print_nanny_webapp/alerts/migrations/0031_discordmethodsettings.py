# Generated by Django 3.1.3 on 2021-02-11 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("alerts", "0030_auto_20210210_1603"),
    ]

    operations = [
        migrations.CreateModel(
            name="DiscordMethodSettings",
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
                ("created_dt", models.DateTimeField(auto_now_add=True)),
                ("updated_dt", models.DateTimeField(auto_now=True)),
                (
                    "target_id",
                    models.CharField(
                        db_index=True,
                        help_text='ID to send notifications to\nTo get an item\'s ID, enable developer mode on under Discord Settings -> Appearance and right click to the target it (ex. a channel or a user) and "Copy ID"',
                        max_length=24,
                    ),
                ),
                (
                    "target_id_type",
                    models.CharField(
                        choices=[
                            ("USER", "User to send a direct message to"),
                            ("CHANNEL", "A channel to send a message to"),
                        ],
                        db_index=True,
                        max_length=255,
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
