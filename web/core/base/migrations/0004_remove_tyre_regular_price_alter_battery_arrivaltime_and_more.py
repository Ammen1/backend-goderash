# Generated by Django 4.2.8 on 2023-12-27 21:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_battery_regular_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tyre',
            name='regular_price',
        ),
        migrations.AlterField(
            model_name='battery',
            name='arrivaltime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='battery',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='batteries', to='base.category'),
        ),
    ]
