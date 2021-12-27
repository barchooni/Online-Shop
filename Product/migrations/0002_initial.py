# Generated by Django 4.0 on 2021-12-27 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Product', '0001_initial'),
        ('Salesman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.customer'),
        ),
        migrations.AddField(
            model_name='wishlist',
            name='product',
            field=models.ManyToManyField(to='Product.Product'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product'),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='User.customer'),
        ),
        migrations.AddField(
            model_name='productcomment',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='Product.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='salesman',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Salesman.salesman'),
        ),
        migrations.AddField(
            model_name='category',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.category'),
        ),
        migrations.AddField(
            model_name='cart',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.customer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(to='Product.Product'),
        ),
    ]
