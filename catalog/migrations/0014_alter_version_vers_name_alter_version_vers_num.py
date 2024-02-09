# Generated by Django 4.2.7 on 2024-02-05 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_product_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='vers_name',
            field=models.CharField(default='test', max_length=100, verbose_name='название версии'),
        ),
        migrations.AlterField(
            model_name='version',
            name='vers_num',
            field=models.IntegerField(default=1, verbose_name='номер версии'),
        ),
    ]
