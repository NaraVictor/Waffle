# Generated by Django 3.0.4 on 2020-03-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='date',
            new_name='video_date',
        ),
        migrations.RenameField(
            model_name='video',
            old_name='time',
            new_name='video_time',
        ),
    ]