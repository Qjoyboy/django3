# Generated by Django 5.0 on 2024-01-17 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90, verbose_name='Название')),
                ('slug', models.CharField(max_length=100, verbose_name='Ссылка')),
                ('body', models.TextField(max_length=211, verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, default='test', null=True, upload_to='media/', verbose_name='Превью')),
                ('create_date', models.DateField(blank=True, null=True, verbose_name='дата создания')),
                ('ispublished', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('view_count', models.IntegerField(verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'публикация',
                'verbose_name_plural': 'публикации',
            },
        ),
    ]
