# Generated by Django 5.1.6 on 2025-03-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=80)),
                ('father_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('roll_number', models.BigIntegerField(unique=True)),
                ('math', models.BigIntegerField()),
                ('english', models.BigIntegerField()),
                ('history', models.BigIntegerField()),
                ('science', models.BigIntegerField()),
                ('hindi', models.BigIntegerField()),
                ('total', models.BigIntegerField()),
                ('percentage', models.FloatField()),
                ('result', models.CharField(max_length=20)),
                ('division', models.CharField(max_length=20)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
