# Generated by Django 4.0 on 2022-01-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0010_remove_productcomment_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img',
            field=models.ImageField(null=True, upload_to='category'),
        ),
    ]
