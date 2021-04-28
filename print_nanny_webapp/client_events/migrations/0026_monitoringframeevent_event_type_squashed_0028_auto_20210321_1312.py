# Generated by Django 3.1.7 on 2021-04-28 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0048_auto_20210321_1312'),
        ('client_events', '0025_auto_20210313_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='monitoringframeevent',
            name='event_type',
            field=models.CharField(choices=[('monitoring_frame_raw', 'Monitoring frame sent without model annotations'), ('monitoring_frame_post', 'Monitoring frame sent with on-device annotations')], db_index=True, default='monitoring_frame_raw', max_length=255),
        ),
        migrations.DeleteModel(
            name='MonitoringFrameEvent',
        ),
        migrations.AddField(
            model_name='octoprintevent',
            name='print_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printsession'),
        ),
        migrations.AddField(
            model_name='printjobstate',
            name='print_session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printsession'),
        ),
    ]
