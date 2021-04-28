# Generated by Django 3.1.7 on 2021-04-28 03:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("alerts", "0060_auto_20210427_2013"),
    ]

    operations = [
        migrations.CreateModel(
            name="PrintProgresEventSettings",
            fields=[
                (
                    "alerteventsettings_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="alerts.alerteventsettings",
                    ),
                ),
                (
                    "on_progress_percent",
                    models.IntegerField(
                        default=25,
                        help_text="Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("alerts.alerteventsettings",),
        ),
        migrations.AddField(
            model_name="alerteventsettings",
            name="user",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]