# Generated by Django 3.1.3 on 2021-01-03 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_auto_20210103_0004"),
    ]

    operations = [
        migrations.AlterField(
            model_name="appcard",
            name="static_image",
            field=models.CharField(max_length=255, null=True),
        ),
    ]
