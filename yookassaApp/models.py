from uuid import uuid4

from django.db import models

# Create your models here.
from accounts.models import CustomUser


class TransactionStatus(models.Model):
    name = models.CharField('Название', max_length=35)

    class Meta:
        verbose_name = 'Статус транзакции'
        verbose_name_plural = 'Статусы транзакций'

    def __str__(self):
        return self.name


class Currensy(models.Model):
    """Модель денежных валют (рубли, доллары и другие)."""
    name = models.CharField(unique=True, verbose_name='Название валюты', max_length=25)  # Полное название валюты
    currency_kod = models.CharField(unique=True, verbose_name='Код валюты', max_length=10)  # Короткое название валюты

    class Meta:
        verbose_name = 'Название валюты'
        verbose_name_plural = 'Название валюты'

    def __str__(self):
        return f'{self.name} ({self.currency_kod})'


class Transaction(models.Model):
    transaction_token = models.CharField(verbose_name='Токен', max_length=50, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь',
                             related_name='trasnsaction_users')
    status = models.ForeignKey(TransactionStatus, on_delete=models.CASCADE, verbose_name='Статус',
                               related_name='trasnsaction_statuses', default=1)
    value = models.FloatField(verbose_name='Цена', default=0)
    currency = models.ForeignKey(Currensy, on_delete=models.SET_DEFAULT, verbose_name='Вид валюты',
                                 related_name='currency_transactions', default=1)  # Вид валюты
    created_at = models.DateTimeField(verbose_name='Транзация создана', auto_now=True)
    updated_at = models.DateTimeField(verbose_name='Последние изменение', auto_now=True)

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f'{self.user} - {self.value} ({self.currency.currency_kod}) | {self.updated_at}'


class RefundStatus(models.Model):
    name = models.CharField('Название', max_length=35)

    class Meta:
        verbose_name = 'Статус возврата'
        verbose_name_plural = 'Статусы возврата'

    def __str__(self):
        return self.name


class Refund(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, verbose_name='Пользователь')
    refund_token = models.CharField(verbose_name='Токен', max_length=50, primary_key=True, blank=True)
    status = models.ForeignKey(TransactionStatus, on_delete=models.CASCADE, verbose_name='Статус',
                               related_name='refund_statuses', default=1)
    value = models.FloatField(verbose_name='Цена', default=0)

    currency = models.ForeignKey(Currensy, on_delete=models.SET_DEFAULT, verbose_name='Вид валюты',
                                 related_name='currency_refunds', default=1)
    created_at = models.DateTimeField(verbose_name='Транзация создана', auto_now=True)
    updated_at = models.DateTimeField(verbose_name='Последние изменение', auto_now=True)
    description = models.TextField('Описание', blank=True)

    def __str__(self):
        return f'{self.transaction.user} - {self.value} ({self.currency.currency_kod}) | {self.updated_at}'


    class Meta:
        verbose_name = 'Возврат'
        verbose_name_plural = 'Возвраты'
