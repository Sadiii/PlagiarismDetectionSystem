# Generated by Django 2.0.4 on 2018-07-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plagtrace', '0035_contact_reg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='reg',
        ),
        migrations.AddField(
            model_name='contact',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='username',
            field=models.TextField(default=None, max_length=200),
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
