# Generated by Django 4.0 on 2022-01-26 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_userdevice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdevice',
            old_name='browser_type',
            new_name='check_field',
        ),
        migrations.RenameField(
            model_name='userdevice',
            old_name='browser_version',
            new_name='device_brand',
        ),
        migrations.RemoveField(
            model_name='userdevice',
            name='os_version',
        ),
        migrations.RemoveField(
            model_name='userdevice',
            name='session',
        ),
    ]
