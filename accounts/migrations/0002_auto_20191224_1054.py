# Generated by Django 2.2.5 on 2019-12-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simple',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='simple',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
