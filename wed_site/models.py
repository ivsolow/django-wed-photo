from django.db import models
from django.urls import reverse
from datetime import date


class MainPhotos(models.Model):
    """Фотографии главной страницы"""
    image = models.ImageField(upload_to='photos', verbose_name='My Photo')

    def __str__(self):
        return str(self.image.name.split('.')[-2])

    class Meta:
        verbose_name = 'Фотография главной страницы'
        verbose_name_plural = 'Фотографии главной страницы'


class LoveStories(models.Model):
    """Фотографии lovestory"""
    image = models.ImageField(upload_to='lovestories', verbose_name='lovestories')

    def __str__(self):
        return str(self.image.name.split('.')[-2])

    class Meta:
        verbose_name = 'Lovestory'
        verbose_name_plural = 'Lovestories'


class WedPost(models.Model):
    """
    Пост с фотографиями, с возможностью загружать несколько фото
    """
    title = models.CharField('Название серии', max_length=250)
    cover = models.ImageField(upload_to='covers', null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default='slug_')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('wedpost', kwargs={'wedpost_slug': self.slug})

    class Meta:
        verbose_name = 'Свадебная серия'
        verbose_name_plural = 'Свадебные серии'
        ordering = ['title', ]


def case_upload_location(instance, filename):
    """
    Cоздает папку для храниения фото поста,
    которая называется также, как и пост
    """
    case_name = instance.wedpost.title.lower().replace(" ", "-")
    file_name = filename.lower().replace(" ", "-")
    return "img/{}/{}".format(case_name, file_name)


class ImgSeries(models.Model):
    """Храниение всех фотографий из всех постов"""
    wedpost = models.ForeignKey(WedPost, on_delete=models.CASCADE) 
    image = models.ImageField(upload_to='case_upload_location', null=True, blank=True)

    def __str__(self):
        if len(str(self.pk)) <= 1:
            number = '00' + str(self.pk)
        elif len(str(self.pk)) == 2:
            number = '0' + str(self.pk)
        else:
            number = str(self.pk)
        return self.wedpost.title + number

    class Meta:
        verbose_name = 'Фотография сведебной серии'
        verbose_name_plural = 'Фотографии свадебной серии'
        ordering = ['id', ]


class Feedback(models.Model):
    """Отзывы"""
    name = models.CharField('Имена пары', max_length=100)
    city = models.CharField('Город', max_length=30, null=True, default='Москва')
    date = models.DateField(auto_now=False, default=date.today)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    content = models.CharField('Текст отзыва', max_length=2500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

