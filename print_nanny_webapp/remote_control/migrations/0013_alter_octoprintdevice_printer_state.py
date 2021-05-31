# Generated by Django 3.2.2 on 2021-05-31 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0012_alter_octoprintdevice_printer_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='octoprintdevice',
            name='printer_state',
            field=models.CharField(choices=[('Pperational', 'Printer Connected'), ('Paused', 'Paused'), ('Cancelling', 'Cancelling'), ('Printing', 'Printing'), ('Pausing', 'Pausing'), ('sdReady', 'SD Card Available'), ('Error', 'Error'), ('ReadyPrinter Ready', 'Ready'), ('closedOrError', 'Printer Connection Closed'), ('Offline', 'Printer Offline'), ('Opening serial connection', 'Opening serial connection')], db_index=True, default='Offline', max_length=36),
        ),
    ]
