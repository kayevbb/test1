from django.db import models
from django.urls import reverse
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from typing import Any


GENDER_CHOICES = [
    ['male', u"Крытай"],
    ['female', u"Не крытый"],
]


class Fields(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    user_name = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Полное имя")
    avatar = models.ImageField(upload_to='')
    address = models.CharField(max_length=60, blank=True, null=True, verbose_name=u'адрес')
    phone_number = models.CharField(max_length=14, blank=True, null=True, verbose_name='номер')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Описание поля")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")
    gender = models.CharField(max_length=10, verbose_name=u"Полe", choices=GENDER_CHOICES, default="male")


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])