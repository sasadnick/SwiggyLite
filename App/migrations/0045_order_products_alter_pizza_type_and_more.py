# Generated by Django 4.2.4 on 2024-03-29 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0043_southindian_soups_sauce_roll_pizza_fingerfood_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
