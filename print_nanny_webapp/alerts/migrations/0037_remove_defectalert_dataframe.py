# Generated by Django 3.1.7 on 2021-03-21 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0036_auto_20210321_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defectalert',
            name='dataframe',
        ),
    ]