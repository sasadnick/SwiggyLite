# Generated by Django 4.2.5 on 2023-10-11 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_alter_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='Alcholic', on_delete=django.db.models.deletion.CASCADE, to='App.category'),
        ),
    ]
