# Generated by Django 2.0.4 on 2018-07-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagtrace', '0033_auto_20180704_0443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=500)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
