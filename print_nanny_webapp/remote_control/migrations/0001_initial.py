# Generated by Django 3.1.3 on 2020-11-20 20:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GcodeFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='uploads/gcode_file/%Y/%m/%d/')),
                ('file_hash', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'file_hash')},
            },
        ),
        migrations.CreateModel(
            name='PrinterProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('axes_e_inverted', models.BooleanField()),
                ('axes_e_speed', models.IntegerField()),
                ('axes_x_speed', models.IntegerField()),
                ('axes_x_inverted', models.BooleanField()),
                ('axes_y_inverted', models.BooleanField()),
                ('axes_y_speed', models.IntegerField()),
                ('axes_z_inverted', models.BooleanField()),
                ('axes_z_speed', models.IntegerField()),
                ('extruder_count', models.IntegerField()),
                ('extruder_nozzle_diameter', models.FloatField()),
                ('extruder_shared_nozzle', models.BooleanField()),
                ('heated_bed', models.BooleanField()),
                ('heated_chamber', models.BooleanField()),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('volume_custom_box', models.BooleanField()),
                ('volume_depth', models.FloatField()),
                ('volume_formfactor', models.CharField(max_length=255)),
                ('volume_height', models.FloatField()),
                ('volume_origin', models.CharField(max_length=255)),
                ('volume_width', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name')},
            },
        ),
        migrations.CreateModel(
            name='PrintJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField()),
                ('name', models.CharField(max_length=255)),
                ('gcode_file_hash', models.CharField(max_length=255, null=True)),
                ('last_status', models.CharField(choices=[('STARTED', 'Started'), ('DONE', 'Done'), ('FAILED', 'Failed'), ('CANCELLING', 'Cancelling'), ('CANCELLED', 'Cancelled'), ('PAUSED', 'Paused'), ('RESUMED', 'Resumed')], default='STARTED', max_length=12)),
                ('last_seen', models.DateTimeField(auto_now=True)),
                ('gcode_file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='remote_control.gcodefile')),
                ('printer_profile', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='remote_control.printerprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'name', 'dt')},
            },
        ),
    ]