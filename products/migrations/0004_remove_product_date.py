# Generated by Django 3.2.6 on 2021-09-03 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='date',
        ),
    ]
