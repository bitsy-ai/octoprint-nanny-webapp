# Generated by Django 3.1.7 on 2021-04-11 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("alerts", "0052_auto_20210411_1421"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="printsessionalertsettings",
            name="needs_review",
        ),
        migrations.AddField(
            model_name="printsessionalert",
            name="needs_review",
            field=models.BooleanField(default=False),
        ),
    ]