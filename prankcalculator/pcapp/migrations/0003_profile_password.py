# Generated by Django 3.0.8 on 2021-05-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcapp', '0002_auto_20210514_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='password',
            field=models.TextField(blank=True),
        ),
    ]