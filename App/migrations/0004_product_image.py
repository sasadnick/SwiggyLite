# Generated by Django 4.2.5 on 2023-10-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_cart_cartitem_category_product_delete_login_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/static/img/404.png', upload_to='media/products/'),
        ),
    ]
