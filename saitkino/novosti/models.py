# Create your models here.
from django.db import models
from datetime import date

# Create your models here.

class Category2(models.Model):
    name = models.CharField('Категория', max_length=150)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'КатегорииНов'
        verbose_name_plural = 'КатегорииНов'


class Actor2(models.Model):
    name = models.CharField('Имя', max_length=100)
    age = models.PositiveSmallIntegerField('Возраст', default=0)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='actors')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и РежисерыНов'
        verbose_name_plural = 'Актеры и РежисерыНов'


class Genre2(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ЖанрНов'
        verbose_name_plural = 'ЖанрыНов'


class Movie2(models.Model):
    title = models.CharField('Название', max_length=100)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    poster = models.ImageField('Постер', upload_to='movies')
    year = models.PositiveSmallIntegerField('Дата Выхода', default=2019)
    country = models.CharField('Страна', max_length=30)
    directors = models.ManyToManyField(Actor2, verbose_name='режиссер', related_name='film_directornews')
    actors = models.ManyToManyField(Actor2, verbose_name='актеры', related_name='film_actornews')
    genres = models.ManyToManyField(Genre2, verbose_name='жанры')
    world_premiere = models.DateField('Примьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0, help_text='указывать сумму в долларах')
    category = models.ForeignKey(Category2, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'ФильмНов'
        verbose_name_plural = 'ФильмыНов'


class MovieShots2(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='movie_shots')
    movie = models.ForeignKey(Movie2, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Кадр из ФильмаНов'
        verbose_name_plural = 'Кадры из ФильмаНов'
