# Generated by Django 5.0 on 2024-01-13 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_category_id_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='test', null=True, upload_to='catalog/', verbose_name='Превью'),
        ),
    ]
