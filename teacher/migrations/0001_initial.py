# Generated by Django 3.0.6 on 2020-08-14 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=244)),
            ],
        ),
        migrations.CreateModel(
            name='Subcat4',
            fields=[
                ('scid', models.AutoField(primary_key=True, serialize=False)),
                ('scname', models.CharField(max_length=255)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Cat')),
            ],
        ),
    ]
