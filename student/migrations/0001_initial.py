# Generated by Django 3.2.8 on 2021-11-02 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stid', models.CharField(max_length=6)),
                ('rno', models.CharField(max_length=6)),
                ('htid', models.CharField(max_length=6)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stid', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('attendance', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hname', models.CharField(max_length=50)),
                ('build_no', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('img', models.FileField(upload_to='file')),
                ('email', models.CharField(max_length=50)),
                ('con', models.CharField(max_length=12)),
                ('wname', models.CharField(max_length=20)),
                ('rno', models.CharField(max_length=5)),
                ('fno', models.CharField(max_length=6)),
                ('rent', models.CharField(max_length=5)),
                ('uname', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('utype', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stid', models.CharField(max_length=6)),
                ('htid', models.CharField(max_length=6)),
                ('amt', models.CharField(max_length=10)),
                ('accno', models.CharField(max_length=20)),
                ('ifsc', models.CharField(max_length=20)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rno', models.CharField(max_length=6)),
                ('stid', models.CharField(max_length=6)),
                ('htid', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Sreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admnno', models.CharField(max_length=10)),
                ('sfname', models.CharField(max_length=20)),
                ('slname', models.CharField(max_length=20)),
                ('stream', models.CharField(max_length=50)),
                ('yoj', models.CharField(max_length=50)),
                ('duration', models.CharField(max_length=10)),
                ('semail', models.EmailField(max_length=50)),
                ('con', models.CharField(max_length=12)),
                ('housename', models.CharField(max_length=12)),
                ('location', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=5)),
                ('pin', models.CharField(max_length=6)),
                ('pname', models.CharField(max_length=20)),
                ('pemail', models.EmailField(max_length=20)),
                ('img', models.FileField(upload_to='file')),
                ('aadhar', models.FileField(upload_to='file')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
