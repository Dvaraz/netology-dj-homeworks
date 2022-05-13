from django.db import models
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='модель')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    image = models.URLField(max_length=200, verbose_name='Изображение')
    release_date = models.DateField(verbose_name='Дата релиза')
    lte_exists = models.BooleanField(verbose_name='LTE')

    def __str__(self):
        return self.name

