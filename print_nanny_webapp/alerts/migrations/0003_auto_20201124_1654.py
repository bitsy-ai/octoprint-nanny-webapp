# Generated by Django 3.1.3 on 2020-11-25 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0002_auto_20201124_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defectalert',
            name='annotated_gif',
        ),
        migrations.RemoveField(
            model_name='timelapsealert',
            name='annotated_gif',
        ),
    ]
