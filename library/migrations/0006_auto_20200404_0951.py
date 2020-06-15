# Generated by Django 3.0.4 on 2020-04-04 08:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('library', '0005_auto_20200404_0917'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VideoFlags',
            new_name='VideoFlag',
        ),
        migrations.RenameModel(
            old_name='VideoViews',
            new_name='VideoView',
        ),
        migrations.AlterField(
            model_name='video',
            name='deleted',
            field=models.BooleanField(default=False, help_text='deleted videos will not show in library n searches'),
        ),
    ]