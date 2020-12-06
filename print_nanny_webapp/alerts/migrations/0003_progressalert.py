# Generated by Django 3.1.3 on 2020-12-06 19:10

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import print_nanny_webapp.alerts.models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0003_printjob_progress'),
        ('alerts', '0002_auto_20201205_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgressAlert',
            fields=[
                ('alertmessage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='alerts.alertmessage')),
                ('job_status', models.CharField(choices=[('Processing', 'Processing'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure')], default='Processing', max_length=32)),
                ('created_dt', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_dt', models.DateTimeField(auto_now=True, db_index=True)),
                ('dataframe', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('original_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('annotated_video', models.FileField(null=True, upload_to=print_nanny_webapp.alerts.models._upload_to)),
                ('feedback', models.BooleanField(null=True)),
                ('length', models.FloatField(null=True)),
                ('fps', models.FloatField(null=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), default=['progress-alert'], size=None)),
                ('print_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('alerts.alertmessage', models.Model),
        ),
    ]