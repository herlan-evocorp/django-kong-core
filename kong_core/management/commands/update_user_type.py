from django.core.management.base import BaseCommand, CommandError
from ...models import Client
from ...utils import get_user_type


class Command(BaseCommand):
    help = 'Update user type'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='all clientes',
            help='Update all clients',
        )

    def handle(self, *args, **options):
        if options['all']:
            for client in Client.objects.all():
                client.user_type = get_user_type(client.id)
                client.save()
        elif client.user_type == None:
            for client in Client.objects.all():
                client.user_type = get_user_type(client.id)
                client.save()
