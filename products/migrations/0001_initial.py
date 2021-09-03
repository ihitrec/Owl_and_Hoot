# Generated by Django 3.2.6 on 2021-09-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('sale_price', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('brand', models.CharField(max_length=20)),
                ('img', models.URLField()),
                ('total_rating', models.DecimalField(decimal_places=0, default=0, max_digits=65)),
                ('num_of_ratings', models.DecimalField(decimal_places=0, default=0, max_digits=65)),
                ('rating', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
                ('gender', models.CharField(max_length=6)),
            ],
        ),
    ]
