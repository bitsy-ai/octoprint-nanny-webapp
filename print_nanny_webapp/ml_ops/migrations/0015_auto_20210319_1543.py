# Generated by Django 3.1.7 on 2021-03-19 22:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("ml_ops", "0014_devicecalibration_dataframe"),
    ]

    operations = [
        migrations.RenameField(
            model_name="devicecalibration",
            old_name="dataframe",
            new_name="config_file",
        ),
    ]
