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

class Blog(models.Model):
    title = models.CharField(max_length=90, verbose_name='Название')
    slug = models.CharField(unique=True,max_length=100,verbose_name='Ссылка')
    body = models.TextField(max_length=211, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='media/', verbose_name='Превью', default='test', **NULLABLE)
    create_date = models.DateField(**NULLABLE,verbose_name='дата создания')
    ispublished = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(verbose_name='количество просмотров',default=0)

    def __str__(self):
        return f'{self.title}, {self.body},{self.ispublished}, {self.preview}, {self.create_date}, {self.ispublished}, {self.slug}'


    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super(Blog,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('blog_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'

