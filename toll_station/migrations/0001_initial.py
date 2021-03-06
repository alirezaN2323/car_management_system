# Generated by Django 4.0.2 on 2022-02-24 20:43

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TollStation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Name')),
                ('toll_per_cross', models.PositiveIntegerField(verbose_name='toll_per_cross')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='location')),
            ],
            options={
                'verbose_name': 'Toll Station',
                'verbose_name_plural': 'Toll Stations',
                'db_table': 'toll_station',
            },
        ),
    ]
