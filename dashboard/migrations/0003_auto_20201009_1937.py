# Generated by Django 3.1.1 on 2020-10-09 11:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20201009_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 19, 37, 52, 739870)),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 19, 37, 52, 739870)),
        ),
    ]
