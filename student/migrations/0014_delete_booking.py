# Generated by Django 3.2.8 on 2021-12-04 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_alter_booking_bdate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='booking',
        ),
    ]
