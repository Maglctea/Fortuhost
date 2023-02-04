from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.manager import CustomUserManager


class CustomUser(AbstractUser):
    # email = models.EmailField(_('email address'), unique=True)
    wallet = models.IntegerField('Баланс', default=0, )

    # REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username