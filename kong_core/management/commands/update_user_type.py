from django.core.management.base import BaseCommand, CommandError
from ...models import Client
from ...utils import get_user_type


class Command(BaseCommand):
    help = 'Update user type'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            help='Update all clients',
        )

    def handle(self, *args, **options):
        if options['all']:
            for client in Client.objects.all():
                client.user_type = get_user_type(client.x_authenticated_userid)
                client.save()
        else:
            for client in Client.objects.all():
                
                if client.user_type == None:
                    client.user_type = get_user_type(client.x_authenticated_userid)
                    client.save()
