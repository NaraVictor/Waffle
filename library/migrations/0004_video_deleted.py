# Generated by Django 3.0.4 on 2020-03-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_video_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
