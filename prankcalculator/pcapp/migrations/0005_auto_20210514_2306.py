# Generated by Django 3.0.8 on 2021-05-14 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0004_profile_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fooled_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='lover_name',
        ),
    ]
