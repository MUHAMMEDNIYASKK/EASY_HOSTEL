# Generated by Django 3.1.7 on 2021-12-11 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0017_auto_20211210_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='hreg',
            name='type',
            field=models.CharField(default='boys', max_length=15),
        ),
        migrations.AddField(
            model_name='sreg',
            name='gender',
            field=models.CharField(default='', max_length=20),
        ),
    ]
