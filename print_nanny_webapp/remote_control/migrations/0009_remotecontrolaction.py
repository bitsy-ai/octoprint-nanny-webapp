# Generated by Django 3.1.3 on 2021-01-03 23:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('remote_control', '0008_octoprintdevice_cloudiot_device_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='RemoteControlAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('action', models.CharField(choices=[('Stop', 'Stop'), ('Pause', 'Pause'), ('Resume', 'Resume')], max_length=255)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='remote_control.octoprintdevice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
