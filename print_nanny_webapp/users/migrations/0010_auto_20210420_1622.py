# Generated by Django 3.1.7 on 2021-04-20 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_geekstoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geekstoken',
            name='token',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
