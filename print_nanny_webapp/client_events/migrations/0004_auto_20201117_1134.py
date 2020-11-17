# Generated by Django 3.1.3 on 2020-11-17 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_events', '0003_auto_20201117_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='printjob',
            name='last_status',
            field=models.CharField(choices=[('STARTED', 'Started'), ('DONE', 'Done'), ('FAILED', 'Failed'), ('CANCELLING', 'Cancelling'), ('CANCELLED', 'Cancelled'), ('PAUSED', 'Paused'), ('RESUMED', 'Resumed')], default='STARTED', max_length=12),
        ),
    ]
