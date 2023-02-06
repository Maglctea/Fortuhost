from django.core.management.base import BaseCommand

from support.models import FeedbackType


def fill_const():
    """ Заполняет таблицу типов обращения в поддержку"""
    FeedbackType.objects.create('Баг')
    FeedbackType.objects.create('Жалоба')
    FeedbackType.objects.create('Предложение')
    FeedbackType.objects.create('Другое')


class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_const()
