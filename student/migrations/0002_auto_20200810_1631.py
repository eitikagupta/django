# Generated by Django 3.0.6 on 2020-08-10 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teststu',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='teststu',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
