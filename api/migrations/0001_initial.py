# Generated by Django 2.1.9 on 2021-09-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('salary', models.CharField(max_length=60)),
                ('location', models.CharField(max_length=125)),
            ],
        ),
    ]