# Generated by Django 3.0.8 on 2021-05-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0003_profile_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='url',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
