# Generated by Django 3.2.8 on 2021-12-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warden', '0003_attendance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance',
            field=models.CharField(default='', max_length=20),
        ),
    ]
