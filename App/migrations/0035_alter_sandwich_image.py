# Generated by Django 4.2.4 on 2024-03-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0034_alter_sandwich_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sandwich',
            name='image',
            field=models.ImageField(default='img/404.png', upload_to='img/'),
        ),
    ]
