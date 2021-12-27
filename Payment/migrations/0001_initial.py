# Generated by Django 4.0 on 2021-12-27 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
                ('cart', models.JSONField(default=dict)),
                ('price', models.CharField(max_length=30)),
                ('payment_method', models.CharField(max_length=30)),
                ('tracking_code', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
