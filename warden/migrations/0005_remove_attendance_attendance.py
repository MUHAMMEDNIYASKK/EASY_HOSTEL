# Generated by Django 3.2.8 on 2021-12-08 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warden', '0004_alter_attendance_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attendance',
        ),
    ]