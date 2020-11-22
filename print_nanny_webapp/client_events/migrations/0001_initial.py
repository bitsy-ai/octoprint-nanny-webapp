# Generated by Django 3.1.3 on 2020-11-22 06:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('remote_control', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictEventFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annotated_image', models.ImageField(upload_to='uploads/predict_event/%Y/%m/%d/')),
                ('hash', models.CharField(max_length=255)),
                ('original_image', models.ImageField(upload_to='uploads/predict_event/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='PredictEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('event_data', models.JSONField(null=True)),
                ('predict_data', models.JSONField()),
                ('plugin_version', models.CharField(max_length=30)),
                ('octoprint_version', models.CharField(max_length=30)),
                ('files', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client_events.predicteventfile')),
                ('print_job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OctoPrintEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(db_index=True)),
                ('event_type', models.CharField(db_index=True, max_length=30)),
                ('event_data', models.JSONField()),
                ('plugin_version', models.CharField(max_length=30)),
                ('octoprint_version', models.CharField(max_length=30)),
                ('print_job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='remote_control.printjob')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
