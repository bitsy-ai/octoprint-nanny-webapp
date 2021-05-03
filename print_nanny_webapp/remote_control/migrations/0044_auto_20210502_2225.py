# Generated by Django 3.1.7 on 2021-05-03 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remote_control', '0043_auto_20210428_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='printsession',
            name='progress',
        ),
        migrations.AddField(
            model_name='printsession',
            name='filepos',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='printsession',
            name='print_progress',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='printsession',
            name='time_elapsed',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='printsession',
            name='time_remaining',
            field=models.IntegerField(null=True),
        ),
    ]