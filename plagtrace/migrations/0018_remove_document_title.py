# Generated by Django 2.0.4 on 2018-04-21 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plagtrace', '0017_auto_20180420_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
    ]
