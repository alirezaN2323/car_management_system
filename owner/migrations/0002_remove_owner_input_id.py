# Generated by Django 4.0.2 on 2022-02-24 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='input_id',
        ),
    ]