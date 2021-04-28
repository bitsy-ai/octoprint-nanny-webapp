# Generated by Django 3.1.7 on 2021-04-27 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("remote_control", "0061_auto_20210425_2253"),
        ("partners", "0007_auto_20210426_2243"),
    ]

    operations = [
        migrations.AlterField(
            model_name="geekstoken",
            name="octoprint_device",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="remote_control.octoprintdevice",
            ),
        ),
    ]