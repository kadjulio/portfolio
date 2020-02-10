# Generated by Django 3.0.2 on 2020-02-10 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweetText', models.CharField(default='NA', max_length=200)),
                ('user', models.CharField(default='NA', max_length=200)),
                ('followers', models.CharField(default='NA', max_length=200)),
                ('date', models.DateField(default='NA', max_length=200)),
                ('location', models.CharField(default='NA', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]
