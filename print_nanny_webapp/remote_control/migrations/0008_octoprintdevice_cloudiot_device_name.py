# Generated by Django 3.1.3 on 2020-12-31 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0007_auto_20201229_2309'),
    ]

    operations = [
        migrations.AddField(
            model_name='octoprintdevice',
            name='cloudiot_device_name',
            field=models.CharField(default='serial-1234', max_length=255),
            preserve_default=False,
        ),
    ]