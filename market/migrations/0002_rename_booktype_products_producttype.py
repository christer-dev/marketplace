# Generated by Django 4.1.5 on 2023-01-30 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='bookType',
            new_name='productType',
        ),
    ]
