# Generated by Django 4.2 on 2023-04-13 12:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
import wed_site.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имена пары')),
                ('city', models.CharField(default='Пенза', max_length=30, null=True, verbose_name='Город')),
                ('date', models.DateField(default=datetime.date.today)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('content', models.CharField(max_length=2500, verbose_name='Текст отзыва')),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='LoveStories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='lovestories', verbose_name='lovestories')),
            ],
            options={
                'verbose_name': 'Lovestory',
                'verbose_name_plural': 'Lovestories',
            },
        ),
        migrations.CreateModel(
            name='MainPhotos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos', verbose_name='My Photo')),
            ],
            options={
                'verbose_name': 'Фотография главной страницы',
                'verbose_name_plural': 'Фотографии главной страницы',
            },
        ),
        migrations.CreateModel(
            name='WedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название серии')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='covers')),
                ('slug', models.SlugField(default='slug_', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Свадебная серия',
                'verbose_name_plural': 'Свадебные серии',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ImgSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=wed_site.models.case_upload_location)),
                ('wedpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wed_site.wedpost')),
            ],
            options={
                'verbose_name': 'Фотография сведебной серии',
                'verbose_name_plural': 'Фотографии свадебной серии',
                'ordering': ['id'],
            },
        ),
    ]