# Generated by Django 4.2.5 on 2023-10-26 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('restaurants', '0005_restaurant_pricelevel'),
        ('user', '0007_remove_customuser_display_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='display_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('user', 'USER'), ('admin', 'ADMIN'), ('blogger', 'BLOGGER')], default='user', max_length=10),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='RestaurantID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(default='user', max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
