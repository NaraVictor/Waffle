# Generated by Django 2.2.7 on 2020-01-06 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20191227_1514'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='errorlogger',
            table='error_logs',
        ),
    ]
