# Generated by Django 2.0.4 on 2018-04-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagtrace', '0019_document_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]