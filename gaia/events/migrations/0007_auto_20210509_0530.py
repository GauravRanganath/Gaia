# Generated by Django 3.2.2 on 2021-05-09 12:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20210508_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 12, 30, 8, 360169, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 9, 12, 30, 8, 360169, tzinfo=utc)),
        ),
    ]