# Generated by Django 3.1.3 on 2021-01-18 18:40

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('remote_control', '0023_auto_20210118_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='printjob',
            name='created_dt',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 1, 18, 18, 40, 9, 137640, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='printjob',
            name='updated_dt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterUniqueTogether(
            name='printjob',
            unique_together={('user', 'name', 'created_dt')},
        ),
        migrations.RemoveField(
            model_name='printjob',
            name='dt',
        ),
    ]