# Generated by Django 3.2.2 on 2021-05-29 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('telemetry', '0007_alter_octoprintevent_event_type'),
    ]

    operations = [
        migrations.DeleteModel('RemoteCommandEvent'),
        migrations.DeleteModel('OctoPrintPluginEvent'),
        migrations.DeleteModel('OctoprintEvent'),
        migrations.DeleteModel('PrintStatusEvent')
    ]