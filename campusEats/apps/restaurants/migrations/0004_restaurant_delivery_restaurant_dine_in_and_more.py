# Generated by Django 4.2.5 on 2023-10-15 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurant_is_open_restaurant_open_dates_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='Delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Dine_in',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Reservable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Serves_beer',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Serves_vegetarian_food',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Serves_wine',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='Takeout',
            field=models.BooleanField(default=False),
        ),
    ]
