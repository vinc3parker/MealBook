from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'List all superusers.'

    def handle(self, *args, **kwargs):
        superusers = User.objects.filter(is_superuser=True)
        self.stdout.write('Superusers:')
        for superuser in superusers:
            self.stdout.write(f'- Username: {superuser.username}, Email: {superuser.email}')
