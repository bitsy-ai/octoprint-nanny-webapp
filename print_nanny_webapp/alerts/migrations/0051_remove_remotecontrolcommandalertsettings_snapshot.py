# Generated by Django 3.1.7 on 2021-04-09 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0050_auto_20210406_2247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='remotecontrolcommandalertsettings',
            name='snapshot',
        ),
    ]
