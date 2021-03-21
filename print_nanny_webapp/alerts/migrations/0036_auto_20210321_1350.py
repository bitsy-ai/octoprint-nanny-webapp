# Generated by Django 3.1.7 on 2021-03-21 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0049_auto_20210321_1313'),
        ('alerts', '0035_defectalertsettings_session'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defectalertsettings',
            name='session',
        ),
        migrations.AddField(
            model_name='defectalert',
            name='monitoring_mode',
            field=models.CharField(choices=[('ACTIVE', 'Active learning pipeline'), ('LITE', 'Lite/offline mode')], default='LITE', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defectalert',
            name='print_job',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='remote_control.printjob'),
        ),
    ]