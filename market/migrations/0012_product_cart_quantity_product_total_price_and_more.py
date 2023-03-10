# Generated by Django 4.1.5 on 2023-02-07 14:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('market', '0011_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cart_quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='user_cart',
            field=models.ManyToManyField(blank=True, related_name='user_cart', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]