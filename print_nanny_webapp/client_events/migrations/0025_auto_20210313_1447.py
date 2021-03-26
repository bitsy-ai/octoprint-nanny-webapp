# Generated by Django 3.1.7 on 2021-03-13 22:47

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.client_events.models


class Migration(migrations.Migration):

    dependencies = [
        ('ml_ops', '0013_auto_20210313_1315'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('remote_control', '0047_remove_printjob_last_status'),
        ('client_events', '0024_auto_20210313_1428'),
    ]

    operations = [

        migrations.RemoveField(
            model_name='octoprintpolymophicbackupmarch2021',
            name='clientevent_ptr',
        ),
        migrations.RemoveField(
            model_name='plugineventpolymophicbackupmarch2021',
            name='clientevent_ptr',
        ),
        migrations.DeleteModel(
            name='ClientEvent',
        ),
        migrations.DeleteModel(
            name='OctoPrintPolymophicBackupMarch2021',
        ),
        migrations.DeleteModel(
            name='PluginEventPolymophicBackupMarch2021',
        ),
        migrations.CreateModel(
            name='MonitoringFrameEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('event_data', models.JSONField(null=True)),
                ('plugin_version', models.CharField(max_length=60)),
                ('client_version', models.CharField(max_length=60)),
                ('octoprint_version', models.CharField(max_length=60)),
                ('ts', models.DateTimeField(db_index=True)),
                ('session', models.CharField(max_length=128)),
                ('image', models.ImageField(upload_to=print_nanny_webapp.client_events.models._upload_to)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
                ('experiment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ml_ops.experiment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OctoPrintEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('event_data', models.JSONField(null=True)),
                ('plugin_version', models.CharField(max_length=60)),
                ('client_version', models.CharField(max_length=60)),
                ('octoprint_version', models.CharField(max_length=60)),
                ('event_type', models.CharField(choices=[('ClientAuthed', 'ClientAuthed'), ('ClientClosed', 'ClientClosed'), ('ClientDeauthed', 'ClientDeauthed'), ('ClientOpened', 'ClientOpened'), ('SettingsUpdated', 'SettingsUpdated'), ('UserLoggedIn', 'User Logged In'), ('UserLoggedOut', 'User Logged Out'), ('FileAdded', 'FileAdded'), ('FileRemoved', 'FileRemoved'), ('FolderAdded', 'FolderAdded'), ('FolderRemoved', 'FolderRemoved'), ('TransferDone', 'TransferDone'), ('TransferFailed', 'TransferFailed'), ('TransferStarted', 'TransferStarted'), ('UpdatedFiles', 'UpdatedFiles'), ('Upload', 'Upload'), ('CaptureDone', 'CaptureDone'), ('CaptureFailed', 'CaptureFailed'), ('CaptureStart', 'CaptureStart'), ('MovieDone', 'MovieDone'), ('MovieFailed', 'MovieFailed'), ('MovieRendering', 'MovieRendering'), ('PostRollEnd', 'PostRollEnd'), ('PostRollStart', 'PostRollStart'), ('SlicingCancelled', 'SlicingCancelled'), ('SlicingDone', 'SlicingDone'), ('SlicingFailed', 'SlicingFailed'), ('SlicingProfileAdded', 'SlicingProfileAdded'), ('SlicingProfileDeleted', 'SlicingProfileDeleted'), ('SlicingProfileModified', 'SlicingProfileModified'), ('SlicingStarted', 'SlicingStarted'), ('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('PrinterReset', 'PrinterReset'), ('PrinterStateChanged', 'PrinterStateChanged'), ('FirmwareData', 'FirmwareData'), ('PrinterProfileAdded', 'PrinterProfileAdded'), ('PrinterProfileDeleted', 'PrinterProfileDeleted'), ('PrinterProfileModified', 'PrinterProfileModified'), ('PrintProgress', 'PrintProgress'), ('plugin_pi_support_throttle_state', 'plugin_pi_support_throttle_state'), ('Shutdown', 'Shutdown'), ('Startup', 'Startup')], db_index=True, max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PluginEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('event_data', models.JSONField(null=True)),
                ('plugin_version', models.CharField(max_length=60)),
                ('client_version', models.CharField(max_length=60)),
                ('octoprint_version', models.CharField(max_length=60)),
                ('event_type', models.CharField(choices=[('device_register_start', 'Device registration started'), ('device_register_done', 'Device registration succeeded'), ('device_register_failed', 'Device registration failed'), ('printer_profile_sync_start', 'Printer profile sync started'), ('printer_profile_sync_done', 'Printer profile sync succeeded'), ('printer_profile_sync_failed', 'Printer profile sync failed')], db_index=True, max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrintJobState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('event_data', models.JSONField(null=True)),
                ('plugin_version', models.CharField(max_length=60)),
                ('client_version', models.CharField(max_length=60)),
                ('octoprint_version', models.CharField(max_length=60)),
                ('event_type', models.CharField(choices=[('Error', 'Error'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted')], db_index=True, max_length=255)),
                ('state', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('current_z', models.FloatField(null=True)),
                ('progress', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('job_data_file', models.CharField(max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
                ('print_job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
