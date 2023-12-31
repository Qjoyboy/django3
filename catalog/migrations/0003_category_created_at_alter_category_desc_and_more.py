# Generated by Django 5.0 on 2023-12-07 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default='2004-12-14 12:12'),
        ),
        migrations.AlterField(
            model_name='category',
            name='desc',
            field=models.CharField(default='test', max_length=150, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(default='1', primary_key=True, serialize=False, verbose_name='Айди'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='test', max_length=90, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='test', max_length=50, verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='create_date',
            field=models.DateField(default='2004-12-14 12:12'),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(default='test', max_length=90, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(default='1', primary_key=True, serialize=False, verbose_name='Айди'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='test', null=True, upload_to='images/', verbose_name='Превью'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_change',
            field=models.DateTimeField(default='2004-12-14 12:12'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='test', max_length=90, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='test', verbose_name='Цена за штуку'),
        ),
    ]
