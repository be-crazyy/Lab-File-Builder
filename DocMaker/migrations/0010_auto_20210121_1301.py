# Generated by Django 3.1.5 on 2021-01-21 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocMaker', '0009_auto_20210119_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiments',
            name='aim',
            field=models.TextField(max_length=115),
        ),
    ]
