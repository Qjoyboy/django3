from django.db import models
from django.urls import reverse
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}
class Blog(models.Model):
    title = models.CharField(max_length=90, verbose_name='Название')
    slug = models.CharField(unique=True, max_length=100, verbose_name='Ссылка', **NULLABLE)
    body = models.TextField(max_length=211, verbose_name='Содержимое')
    preview = models.ImageField(upload_to='media/', verbose_name='Превью', default='test', **NULLABLE)
    create_date = models.DateField(**NULLABLE,verbose_name='дата создания')
    ispublished = models.BooleanField(default=True, verbose_name='опубликовано')
    view_count = models.IntegerField(verbose_name='количество просмотров',default=0)

    def __str__(self):
        return f'{self.title}, {self.body},{self.ispublished}, {self.preview}, {self.create_date}, {self.ispublished}'


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog,self).save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('blog_item', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
