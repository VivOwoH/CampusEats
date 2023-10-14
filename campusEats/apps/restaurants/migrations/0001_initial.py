# Generated by Django 4.2.5 on 2023-10-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('RestaurantID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=255)),
                ('Location', models.CharField(max_length=255, null=True)),
                ('Description', models.CharField(max_length=255, null=True)),
                ('ImageURL', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
