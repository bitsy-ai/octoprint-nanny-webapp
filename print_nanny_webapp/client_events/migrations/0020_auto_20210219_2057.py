# Generated by Django 3.1.3 on 2021-02-20 04:57

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('remote_control', '0047_remove_printjob_last_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('client_events', '0019_remove_printjobevent_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(db_index=True)),
                ('client_event_type', models.CharField(choices=[('plugin', 'OctoPrint Nanny plugin events'), ('octoprint', 'OctoPrint core and bundled plugins events'), ('octoprint_job', 'OctoPrint print job events')], db_index=True, max_length=255)),
                ('event_data', models.JSONField()),
                ('plugin_version', models.CharField(max_length=60)),
                ('octoprint_version', models.CharField(max_length=60)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_client_events.clientevent_set+', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.RemoveField(
            model_name='printjobevent',
            name='device',
        ),
        migrations.RemoveField(
            model_name='printjobevent',
            name='print_job',
        ),
        migrations.RemoveField(
            model_name='printjobevent',
            name='user',
        ),
        migrations.AlterModelOptions(
            name='octoprintevent',
            options={'base_manager_name': 'objects'},
        ),
        migrations.RemoveField(
            model_name='octoprintevent',
            name='created_dt',
        ),
        migrations.RemoveField(
            model_name='octoprintevent',
            name='device',
        ),
        migrations.RemoveField(
            model_name='octoprintevent',
            name='event_data',
        ),
        migrations.RemoveField(
            model_name='octoprintevent',
            name='id',
        ),
        migrations.RemoveField(
            model_name='octoprintevent',
            name='octoprint_version',
        ),
        migrations.RemoveField(
            model_name='octoprintevent',
            name='plugin_version',
        ),
        migrations.RemoveField(
            model_name='octoprintevent',
            name='user',
        ),
        migrations.CreateModel(
            name='PluginEvent',
            fields=[
                ('clientevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client_events.clientevent')),
                ('event_type', models.CharField(choices=[('bounding_box_predict', 'On-device bounding box prediction'), ('monitoring_frame_raw', 'Raw frame buffer sample'), ('monitoring_frame_post', 'Post-processed frame buffer'), ('device_register_start', 'Device registration started'), ('device_register_done', 'Device registration succeeded'), ('device_register_failed', 'Device registration failed'), ('printer_profile_sync_start', 'Printer profile sync started'), ('printer_profile_sync_done', 'Printer profile sync succeeded'), ('printer_profile_sync_failed', 'Printer profile sync failed')], db_index=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('client_events.clientevent',),
        ),
        migrations.CreateModel(
            name='PrintJobState',
            fields=[
                ('clientevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client_events.clientevent')),
                ('event_type', models.CharField(choices=[('Error', 'Error'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted')], db_index=True, max_length=255)),
                ('state', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('current_z', models.FloatField(null=True)),
                ('progress', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('job_data_file', models.CharField(max_length=255)),
                ('print_job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('client_events.clientevent',),
        ),
        migrations.DeleteModel(
            name='ObjectDetectEventImage',
        ),
        migrations.DeleteModel(
            name='PrintJobEvent',
        ),
        migrations.AddField(
            model_name='octoprintevent',
            name='clientevent_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='client_events.clientevent'),
            preserve_default=False,
        ),
    ]