# Generated by Django 4.2.5 on 2023-10-02 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_alter_badge_code_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountedPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_price', models.CharField(default='<s>{{product.price | safe}}</s><strong class="ms-2 text-danger">{{product.get_price_with_discount() | safe}}</strong>', max_length=700)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.product')),
            ],
        ),
    ]
