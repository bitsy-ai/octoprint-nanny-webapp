# Generated by Django 3.2.2 on 2021-05-30 00:02

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('remote_control', '0005_alter_remotecontrolcommand_command'),
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('telemetry', '0008_auto_20210529_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelemetryEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('event_source', models.CharField(choices=[('octoprint', 'Events originating from octoprint'), ('plugin_octoprint_nanny', 'Events originating from Print Nanny octoprint plugin'), ('remote_command', 'Events originating from a remote control command')], default='plugin_octoprint_nanny', max_length=36)),
                ('event_data', models.JSONField(null=True)),
                ('plugin_version', models.CharField(max_length=60)),
                ('client_version', models.CharField(max_length=60)),
                ('octoprint_version', models.CharField(max_length=60)),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('octoprint_job', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('octoprint_device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_telemetry.telemetryevent_set+', to='contenttypes.contenttype')),
                ('print_session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printsession')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='OctoPrintEvent',
            fields=[
                ('telemetryevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='telemetry.telemetryevent')),
                ('event_type', models.CharField(choices=[('ClientAuthed', 'ClientAuthed'), ('ClientClosed', 'ClientClosed'), ('ClientDeauthed', 'ClientDeauthed'), ('ClientOpened', 'ClientOpened'), ('SettingsUpdated', 'SettingsUpdated'), ('UserLoggedIn', 'User Logged In'), ('UserLoggedOut', 'User Logged Out'), ('FileAdded', 'FileAdded'), ('FileRemoved', 'FileRemoved'), ('FolderAdded', 'FolderAdded'), ('FolderRemoved', 'FolderRemoved'), ('TransferDone', 'TransferDone'), ('TransferFailed', 'TransferFailed'), ('TransferStarted', 'TransferStarted'), ('UpdatedFiles', 'UpdatedFiles'), ('Upload', 'Upload'), ('CaptureDone', 'CaptureDone'), ('CaptureFailed', 'CaptureFailed'), ('CaptureStart', 'CaptureStart'), ('MovieDone', 'MovieDone'), ('MovieFailed', 'MovieFailed'), ('MovieRendering', 'MovieRendering'), ('PostRollEnd', 'PostRollEnd'), ('PostRollStart', 'PostRollStart'), ('SlicingCancelled', 'SlicingCancelled'), ('SlicingDone', 'SlicingDone'), ('SlicingFailed', 'SlicingFailed'), ('SlicingProfileAdded', 'SlicingProfileAdded'), ('SlicingProfileDeleted', 'SlicingProfileDeleted'), ('SlicingProfileModified', 'SlicingProfileModified'), ('SlicingStarted', 'SlicingStarted'), ('Connected', 'Connected'), ('Disconnected', 'Disconnected'), ('PrinterReset', 'PrinterReset'), ('FirmwareData', 'FirmwareData'), ('PrinterStateChanged', 'PrinterStateChanged'), ('PrinterProfileAdded', 'PrinterProfileAdded'), ('PrinterProfileDeleted', 'PrinterProfileDeleted'), ('PrinterProfileModified', 'PrinterProfileModified'), ('PrintProgress', 'PrintProgress'), ('plugin_pi_support_throttle_state', 'plugin_pi_support_throttle_state'), ('Shutdown', 'Shutdown'), ('Startup', 'Startup'), ('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted')], db_index=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('telemetry.telemetryevent',),
        ),
        migrations.CreateModel(
            name='PrintNannyPluginEvent',
            fields=[
                ('telemetryevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='telemetry.telemetryevent')),
                ('event_type', models.CharField(choices=[('plugin_octoprint_nanny_monitoring_start', 'Print Nanny Monitoring started'), ('plugin_octoprint_nanny_monitoring_stop', 'Print Nanny Monitoring stopped'), ('plugin_octoprint_nanny_monitoring_reset', 'Print Nanny Monitoring reset'), ('plugin_octoprint_nanny_device_register_start', 'Device registration started'), ('plugin_octoprint_nanny_device_register_done', 'Device registration succeeded'), ('plugin_octoprint_nanny_device_register_failed', 'Device registration failed'), ('device_reset', 'Device identity reset'), ('plugin_octoprint_nanny_printer_profile_sync_start', 'Printer profile sync started'), ('plugin_octoprint_nanny_printer_profile_sync_done', 'Printer profile sync succeeded'), ('plugin_octoprint_nanny_printer_profile_sync_failed', 'Printer profile sync failed'), ('connect_test_rest_api', 'Test connection to REST API'), ('plugin_octoprint_nanny_connect_test_rest_api_failed', 'Test connection to REST API failed'), ('plugin_octoprint_nanny_connect_test_rest_api_success', 'Test connection to REST API success'), ('plugin_octoprint_nanny_connect_test_mqtt_ping', 'Test connection to REST API'), ('plugin_octoprint_nanny_connect_test_mqtt_ping_failed', 'Test connection to REST API failed'), ('plugin_octoprint_nanny_connect_test_mqtt_ping_success', 'Test connection to REST API success'), ('plugin_octoprint_nanny_connect_test_mqtt_pong', 'Test connection to REST API'), ('plugin_octoprint_nanny_connect_test_mqtt_pong_failed', 'Test connection to REST API failed'), ('plugin_octoprint_nanny_connect_test_mqtt_pong_success', 'Test connection to REST API success')], db_index=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('telemetry.telemetryevent',),
        ),
        migrations.CreateModel(
            name='PrintStatusEvent',
            fields=[
                ('telemetryevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='telemetry.telemetryevent')),
                ('event_type', models.CharField(choices=[('PrintCancelled', 'PrintCancelled'), ('PrintCancelling', 'PrintCancelling'), ('PrintDone', 'PrintDone'), ('PrintFailed', 'PrintFailed'), ('PrintPaused', 'PrintPaused'), ('PrintResumed', 'PrintResumed'), ('PrintStarted', 'PrintStarted')], db_index=True, max_length=255)),
                ('state', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('current_z', models.FloatField(null=True)),
                ('progress', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('job_data_file', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('telemetry.telemetryevent',),
        ),
        migrations.CreateModel(
            name='RemoteCommandEvent',
            fields=[
                ('telemetryevent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='telemetry.telemetryevent')),
                ('event_type', models.CharField(choices=[('remote_command_received', 'Command was received by device'), ('remote_command_failed', 'Command failed. Please download your Octoprint logs and open a Github issue to get this fixed.'), ('remote_command_success', 'Command succeeded')], db_index=True, max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('telemetry.telemetryevent',),
        ),
    ]