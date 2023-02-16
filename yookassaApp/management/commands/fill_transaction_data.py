from django.core.management.base import BaseCommand

from yookassaApp.models import TransactionStatus, Currensy, RefundStatus


def fill_transactionStatus_const():
    """ Заполняет таблицу статусов активности приложения"""
    TransactionStatus.objects.create(name='pending')
    TransactionStatus.objects.create(name='waiting_for_capture')
    TransactionStatus.objects.create(name='succeeded')
    TransactionStatus.objects.create(name='canceled')


def fill_refundStatus_const():
    """ Заполняет таблицу статусов активности приложения"""
    RefundStatus.objects.create(name='canceled')
    RefundStatus.objects.create(name='succeeded')
    RefundStatus.objects.create(name='pending')


def fill_currency_const():
    """ Заполняет таблицу статусов активности приложения"""
    Currensy.objects.create(name='Рубль', currency_kod='RUB')
    Currensy.objects.create(name='Доллар', currency_kod='USD')
    Currensy.objects.create(name='Евро', currency_kod='EUR')


class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_transactionStatus_const()
        fill_refundStatus_const()
        fill_currency_const()
