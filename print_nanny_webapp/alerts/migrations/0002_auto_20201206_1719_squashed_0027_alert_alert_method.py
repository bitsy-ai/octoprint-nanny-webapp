# Generated by Django 3.1.7 on 2021-04-28 17:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models
import print_nanny_webapp.utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0001_initial'),
        ('remote_control', '0003_printjob_progress'),
        ('remote_control', '0019_auto_20210109_2034'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertvideomessage',
            name='job_status',
            field=models.CharField(choices=[('Processing', 'Processing'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('CANCELLED', 'Cancelled')], default='Processing', max_length=32),
        ),
        migrations.RemoveField(
            model_name='timelapsealert',
            name='notify_seconds',
        ),
        migrations.RemoveField(
            model_name='timelapsealert',
            name='notify_timecode',
        ),
        migrations.AddField(
            model_name='alertvideomessage',
            name='notify_seconds',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='alertvideomessage',
            name='notify_timecode',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterModelOptions(
            name='progressalert',
            options={},
        ),
        migrations.AddField(
            model_name='progressalert',
            name='progress',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, db_index=True)),
                ('dismissed', models.BooleanField(default=False)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_alerts.alert_set+', to='contenttypes.contenttype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('seen', models.BooleanField(default=False)),
                ('alert_type', models.CharField(choices=[('COMMAND', 'Remote command status updates'), ('PRINT_PROGRESS', 'Percentage-based print progress'), ('MANUAL_VIDEO_UPLOAD', 'Manually-uploaded video is ready for review'), ('DEFECT', 'Defect detected in print')], default='ALERT', max_length=255)),
                ('alert_method', models.CharField(choices=[('UI', 'Recive Print Nanny UI notifations'), ('EMAIL', 'Receive email notifications')], default='UI', max_length=255)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.RemoveField(
            model_name='alertvideomessage',
            name='polymorphic_ctype',
        ),
        migrations.RemoveField(
            model_name='alertvideomessage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='defectalert',
            name='alertvideomessage_ptr',
        ),
        migrations.RemoveField(
            model_name='defectalert',
            name='print_job',
        ),
        migrations.AlterUniqueTogether(
            name='progressalert',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='progressalert',
            name='alertvideomessage_ptr',
        ),
        migrations.RemoveField(
            model_name='progressalert',
            name='print_job',
        ),
        migrations.RemoveField(
            model_name='timelapsealert',
            name='alertvideomessage_ptr',
        ),
        migrations.DeleteModel(
            name='AlertPlot',
        ),
        migrations.DeleteModel(
            name='AlertVideoMessage',
        ),
        migrations.DeleteModel(
            name='DefectAlert',
        ),
        migrations.DeleteModel(
            name='ProgressAlert',
        ),
        migrations.DeleteModel(
            name='TimelapseAlert',
        ),
        migrations.CreateModel(
            name='ManualVideoUploadAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
                ('job_status', models.CharField(choices=[('Processing', 'Processing'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('CANCELLED', 'Cancelled')], default='Processing', max_length=32)),
                ('dataframe', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('original_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('annotated_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('feedback', models.BooleanField(null=True)),
                ('length', models.FloatField(null=True)),
                ('fps', models.FloatField(null=True)),
                ('notify_seconds', models.IntegerField(null=True)),
                ('notify_timecode', models.CharField(max_length=32, null=True)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alert',),
        ),
        migrations.CreateModel(
            name='AlertPlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('html', models.FileField(upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('title', models.CharField(max_length=65)),
                ('description', models.CharField(max_length=255)),
                ('function', models.CharField(max_length=65)),
                ('alert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alerts.manualvideouploadalert')),
            ],
        ),
        migrations.CreateModel(
            name='AlertSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, db_index=True)),
                ('alert_type', models.CharField(choices=[('COMMAND', 'Remote command status updates'), ('PRINT_PROGRESS', 'Percentage-based print progress'), ('MANUAL_VIDEO_UPLOAD', 'Manually-uploaded video is ready for review'), ('DEFECT', 'Defect detected in print')], max_length=255)),
                ('enabled', models.BooleanField(default=True, help_text='Enable or disable this alert channel')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_alerts.alertsettings_set+', to='contenttypes.contenttype')),
                ('alert_methods', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('UI', 'Recive Print Nanny UI notifations'), ('EMAIL', 'Receive email notifications')], max_length=255), blank=True, default=('UI',), size=None)),
            ],
            options={
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='DefectAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alert',),
        ),
        migrations.CreateModel(
            name='ProgressAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
                ('progress_percent', models.IntegerField(default=25, help_text='Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alert',),
        ),
        migrations.CreateModel(
            name='RemoteControlCommandAlert',
            fields=[
                ('alert_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alert')),
                ('alert_subtype', models.CharField(choices=[('RECEIVED', 'Command was received by'), ('SUCCESS', 'Command succeeded'), ('FAILED', 'Command failed')], default='RECEIVED', max_length=255)),
                ('command', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='remote_control.remotecontrolcommand')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alert',),
        ),
        migrations.CreateModel(
            name='DefectAlertSettings',
            fields=[
                ('alertsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alertsettings')),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alertsettings',),
        ),
        migrations.CreateModel(
            name='ProgressAlertSettings',
            fields=[
                ('alertsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alertsettings')),
                ('on_progress_percent', models.IntegerField(default=25, help_text='Progress notification interval. Example: 25 will notify you at 25%, 50%, 75%, and 100% progress', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alertsettings',),
        ),
        migrations.CreateModel(
            name='RemoteControlCommandAlertSettings',
            fields=[
                ('alertsettings_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alertsettings')),
                ('move_nozzle', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED',), help_text='Fires on <strong>MoveNozzle</strong>command status changes. Helpful for debugging connectivity between Print Nanny and OctoPrint', size=None)),
                ('pause_print', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED',), help_text='Fires on <strong>PausePrint</strong> command status changes. Helpful for verifying a print was paused successfully.', size=None)),
                ('resume_print', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED',), help_text='Fires on <strong>ResumePrint</strong> command status changes Helpful for verifying a print was resumed.', size=None)),
                ('start_monitoring', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED',), help_text='Fires on <strong>StopMonitoring</strong> updates. Helpful if you want to confirm monitoring started without a problem.', size=None)),
                ('start_print', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED',), help_text='Fires on <strong>SartPrint</strong> command status changes. Helpful for verifying a print job started without a problem.', size=None)),
                ('stop_monitoring', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED',), help_text='Fires on <strong>StopMonitoring<strong> updates. \n Helps debug unexpected Print Nanny crashes.', size=None)),
                ('stop_print', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED',), help_text='Fires on <strong>StopPrint</strong> updates. Get notifed as soon as a print job finishes. ', size=None)),
                ('user', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user')),
                ('snapshot', print_nanny_webapp.utils.fields.ChoiceArrayField(base_field=models.CharField(choices=[('RECEIVED', 'Command was acknowledged by device'), ('FAILED', 'Command failed'), ('SUCCESS', 'Command succeeded')], max_length=255), blank=True, default=('FAILED', 'SUCCESS'), help_text='Fires on web camera <strong>Snapshot</strong> command', size=None)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alertsettings',),
        ),
    ]
