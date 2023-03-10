# Generated by Django 4.1.5 on 2023-02-07 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0016_remove_product_price_remove_product_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]