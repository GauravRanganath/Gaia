# Generated by Django 3.2.1 on 2021-05-08 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='Event',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='address',
            new_name='event',
        ),
    ]
