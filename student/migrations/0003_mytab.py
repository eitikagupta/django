# Generated by Django 3.0.6 on 2020-08-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200810_1631'),
    ]

    operations = [
        migrations.CreateModel(
            name='mytab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
