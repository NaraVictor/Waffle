# Generated by Django 2.2.5 on 2019-12-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]