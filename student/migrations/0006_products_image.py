# Generated by Django 3.0.6 on 2020-08-27 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image',
            field=models.ImageField(default='blank.png', upload_to='products/'),
        ),
    ]