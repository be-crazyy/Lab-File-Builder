# Generated by Django 3.1.5 on 2021-01-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocMaker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiments',
            name='experiment_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
