from django.db import models
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=90, verbose_name='Наименование', default='test')
    desc = models.CharField(max_length=90, verbose_name='Описание', default='test')
    image = models.ImageField(upload_to='media/', verbose_name='Превью', default='test', **NULLABLE)
    category = models.CharField(max_length=50, verbose_name='категория', default='test')
    price = models.IntegerField(verbose_name='Цена за штуку', default='test')
    create_date = models.DateField(**NULLABLE)
    last_change = models.DateTimeField(**NULLABLE)
    # id = models.IntegerField(primary_key=True, verbose_name='Айди', default=1)

    def __str__(self):
        return f'{self.name},{self.desc},{self.image},{self.category},{self.price},{self.create_date},{self.last_change}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=90, verbose_name='Наименование', default='test')
    desc = models.CharField(max_length=150, verbose_name='Описание', default='test')
    #created_at = models.DateTimeField(**NULLABLE)
    # id = models.IntegerField(primary_key=True, verbose_name='Айди', default=1)

    def __str__(self):
        return f'{self.name}: {self.desc}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Version(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    vers_num = models.IntegerField(verbose_name='номер версии')
    vers_name = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(verbose_name='актив версии',default=True)

    def __str__(self):
        return f'{self.prod}, {self.vers_name},{self.vers_num}, {self.is_active}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'

