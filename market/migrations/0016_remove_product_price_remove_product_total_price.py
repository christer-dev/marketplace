# Generated by Django 4.1.5 on 2023-02-07 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0015_alter_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='total_price',
        ),
    ]