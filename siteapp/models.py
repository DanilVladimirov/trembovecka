import os
import random
from django.db import models
from django import forms
from django.contrib.auth.models import User


def file_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return f'{basefilename}_{randomstr}{file_extension}'


class Post(models.Model):
    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Події і Новини'
    CHOICES = (
        ('main', 'новина'),
        ('achive', 'досягнення')
    )
    title = models.CharField(max_length=50, default='', blank=True)
    text = models.TextField(default='', blank=True)
    photo = models.ImageField(upload_to=file_path, default=None, null=True, blank=True)
    type_post = models.CharField(choices=CHOICES, default='', max_length=50)

    def __str__(self):
        return self.title


class File(models.Model):
    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файли'
    title = models.CharField(max_length=50, default='')
    url = models.FileField(upload_to=file_path, default=None, blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
    title = models.CharField(max_length=50, default='', blank=True)
    files = models.ManyToManyField(File)

    def __str__(self):
        return self.title


class ConsultationDate(models.Model):
    class Meta:
        verbose_name = 'День консультації'
        verbose_name_plural = 'Дні консультації'
    day = models.CharField(max_length=2)
    time = models.TimeField(default=None)

    def __str__(self):
        return f'{self.day} - {self.time}'


class Images(models.Model):
    img = models.ImageField()


class News(models.Model):
    title = models.CharField(max_length=250, default='')
    text = models.TextField(default='')
    imgs = models.ManyToManyField(Images)

    def __str__(self):
        return self.title


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.TextField(default='')

    def __str__(self):
        return self.text[:15]


class Theme(models.Model):
    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Теми'
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, default='')
    text = models.TextField(default='')
    message = models.ManyToManyField(Message)

    def __str__(self):
        return self.title


class GroupPage(models.Model):
    class Meta:
        verbose_name = 'Сторінка групи'
        verbose_name_plural = 'Сторінка групи'
    main_img = models.ImageField(upload_to=file_path)
    text = models.TextField(default='')

    def __str__(self):
        return 'сторінка групи'


class StartPage(models.Model):
    class Meta:
        verbose_name = 'Головна сторінка'
        verbose_name_plural = 'Головна сторінка'
    text = models.TextField(default='')

    def __str__(self):
        return 'головна сторінка'
