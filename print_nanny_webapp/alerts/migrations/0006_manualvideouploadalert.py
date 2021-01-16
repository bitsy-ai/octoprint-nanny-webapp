# Generated by Django 3.1.3 on 2021-01-11 06:03

from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0005_auto_20210110_2202'),
    ]

    operations = [
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
    ]