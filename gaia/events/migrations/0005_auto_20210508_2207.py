# Generated by Django 3.2.2 on 2021-05-09 05:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20210508_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='<noname>', max_length=255)),
                ('email', models.CharField(default='<noemail>', max_length=255)),
                ('phone_number', models.CharField(max_length=12)),
                ('location', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 5, 7, 7, 378416, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='host_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='event',
            name='long_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='short_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 5, 7, 7, 378416, tzinfo=utc)),
        ),
    ]
