# Generated by Django 3.2.8 on 2021-11-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='status',
            field=models.CharField(default='', max_length=50),
        ),
    ]
