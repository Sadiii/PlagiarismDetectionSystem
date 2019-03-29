# Generated by Django 2.0.2 on 2018-04-12 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2000)),
            ],
        ),
    ]