# Generated by Django 3.1.1 on 2020-10-09 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvd',
            name='date_registered',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 19, 31, 58, 355862)),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='released_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 9, 19, 31, 58, 355862)),
        ),
    ]
