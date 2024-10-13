# Generated by Django 4.2 on 2023-04-27 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_remove_product_main_image_product_logo_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0002_alter_usercart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='products.product'),
        ),
        migrations.AlterField(
            model_name='usercart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to=settings.AUTH_USER_MODEL),
        ),
    ]
