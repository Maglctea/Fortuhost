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


class AppStatus(models.Model):
    status = models.CharField('Название', max_length=50)
    color = models.CharField('Цвет', max_length=10, default='#e6a930')
    permission_start = models.BooleanField('Старт', default=False)
    permission_stop = models.BooleanField('Стоп', default=False)
    permission_restart = models.BooleanField('Рестарт', default=False)
    permission_delete = models.BooleanField('Удалить', default=False)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.status


class App(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='users')
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', blank=True)
    docker_id = models.CharField('ID контейнера', max_length=100, blank=True)
    time_create = models.DateTimeField('Время создания', auto_now_add=True)
    time_update = models.DateTimeField('Время обновления', auto_now=True)
    time_start = models.DateTimeField('Время запуска', auto_now=True)
    app_status = models.ForeignKey(AppStatus, on_delete=models.PROTECT, verbose_name='Статус', related_name='users', default=3)

    class Meta:
        verbose_name = "Приложение"
        verbose_name_plural = "Приложения"

    def __str__(self):
        return self.title



