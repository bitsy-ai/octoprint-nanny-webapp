# Generated by Django 3.2.2 on 2021-06-25 04:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("subscriptions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="memberbadge",
            name="created_dt",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="memberbadge",
            name="updated_dt",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="memberbadge",
            name="type",
            field=models.CharField(
                choices=[
                    (
                        "FreeBeta",
                        "Participated in free beta program between January 2021 - July 2021",
                    ),
                    (
                        "PaidBeta",
                        "Participated in paid beta program starting July 2021",
                    ),
                ],
                max_length=24,
            ),
        ),
        migrations.AlterField(
            model_name="memberbadge",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="member_badges",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]