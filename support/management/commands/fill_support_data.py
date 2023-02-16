from django.core.management.base import BaseCommand

from support.models import FeedbackType


def fill_const():
    """ Заполняет таблицу типов обращения в поддержку"""
    FeedbackType.objects.create(name='Баг')
    FeedbackType.objects.create(name='Жалоба')
    FeedbackType.objects.create(name='Предложение')
    FeedbackType.objects.create(name='Другое')


class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_const()
