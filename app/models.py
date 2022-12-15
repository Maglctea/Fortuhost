from django.contrib.auth.models import AbstractUser
from django.db import models

from app.manager import CustomUserManager
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    wallet = models.IntegerField('Баланс', default=0, )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class App(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='users')
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)
    file = models.FileField(upload_to='upload/', verbose_name='Файл')
    time_create = models.DateTimeField('Время создания', auto_now_add=True)
    time_update = models.DateTimeField('Время обновления', auto_now=True)
    time_start = models.DateTimeField('Время запуска', auto_now=True)
    is_run = models.BooleanField('Запущен', default=True)

    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"

    def __str__(self):
        return self.title