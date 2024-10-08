# Generated by Django 4.2.5 on 2023-10-11 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_alter_product_image_delete_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/static/img/404.png', upload_to='static/img/'),
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_price', models.CharField(default='<s>{{product.price | safe}}</s><strong class="ms-2 text-danger">{{product.get_price_with_discount() | safe}}</strong>', max_length=700)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reverse', to='App.product')),
            ],
        ),
    ]
