from django.core.management.base import BaseCommand

from app.models import AppStatus


def fill_const():
    """ Заполняет таблицу статусов активности приложения"""
    AppStatus.objects.create(status='Отключен', color='#eb4034', permission_start=True, permission_stop=False,
                             permission_restart=False, permission_delete=True)
    AppStatus.objects.create(status='Включен', color='#3dd474', permission_start=False, permission_stop=True,
                             permission_restart=True, permission_delete=False)
    AppStatus.objects.create(status='Перезагрузка', color='#3a71ba', permission_start=False, permission_stop=False,
                             permission_restart=False, permission_delete=False)


class Command(BaseCommand):
    def handle(self, *args, **options):
        fill_const()
