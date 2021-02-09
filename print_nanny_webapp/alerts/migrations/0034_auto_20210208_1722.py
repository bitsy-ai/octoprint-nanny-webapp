# Generated by Django 3.1.3 on 2021-02-09 01:22

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0033_auto_20210203_1710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discordmethodsettings',
            name='channel_id',
        ),
        migrations.AddField(
            model_name='discordmethodsettings',
            name='channel_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='Channel IDs to send notifications to\nTo get your channel ID, enable developer mode on under Discord Settings -> Appearance and right click the channel and "Copy ID"', max_length=24), default=list, size=None),
        ),
        migrations.AddField(
            model_name='discordmethodsettings',
            name='user_ids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(help_text='User IDs to send notifications (as direct messages) to\nTo get your channel ID, enable developer mode on under Discord Settings -> Appearance and right click the channel and "Copy ID"', max_length=24), default=list, size=None),
        ),
    ]