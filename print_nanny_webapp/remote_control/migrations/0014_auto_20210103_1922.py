# Generated by Django 3.1.3 on 2021-01-04 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0013_auto_20210103_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remotecontrolcommand',
            name='command',
            field=models.CharField(choices=[('WakePrintNanny', 'Wake Up Print Nanny'), ('StartPrint', 'Start Print'), ('MoveNozzle', 'Move Nozzle'), ('StopPrint', 'Stop Print'), ('PausePrint', 'Pause Print'), ('ResumePrint', 'Resume Print')], max_length=255),
        ),
    ]
