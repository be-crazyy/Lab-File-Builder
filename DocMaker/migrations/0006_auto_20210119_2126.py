# Generated by Django 3.1.5 on 2021-01-19 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocMaker', '0005_auto_20210119_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiments',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 19, 21, 26, 55, 908520)),
        ),
    ]
