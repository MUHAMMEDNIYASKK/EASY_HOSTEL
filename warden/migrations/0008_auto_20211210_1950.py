# Generated by Django 3.1.7 on 2021-12-11 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warden', '0007_auto_20211210_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Hid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='Sid',
            field=models.IntegerField(default=0),
        ),
    ]