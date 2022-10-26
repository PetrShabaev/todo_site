from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):
    help = 'Create some users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Quantity of users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            User.objects.create_user(username=input(f'Введите username пользователя номер {i+1} '),
                                     password=input(f'Введите пароль для пользователя номер {i + 1} '),
                                     first_name=input(f'Введите имя пользователя номер {i+1} '),
                                     last_name=input(f'Введите фамилию пользователя номер {i + 1} '),
                                     email=input(f'Введите email пользователя номер {i + 1} '))
        print('ATTENTION!CREATE SUPERUSER PROCESS')
        User.objects.create_superuser(username=input(f'Введите username '),
                                     password=input(f'Введите пароль '),
                                     email=input(f'Введите email '))
