# Generated by Django 3.1.7 on 2021-03-14 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client_events', '0026_monitoringframeevent_event_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonitoringFrameEvent',
        ),
    ]