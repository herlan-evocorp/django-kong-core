from django.utils.deprecation import MiddlewareMixin
from .models import Client


class KongClientMiddleware(MiddlewareMixin):
    def process_request(self, request):
        headers = request.headers

        if headers is not None and headers.get('X-Consumer-ID', False):
            client = Client.objects.get(pk=headers.get('X-Consumer-ID'))

            if client is not None:
                client, created = Client.objects.get_or_create(
                    x_consumer_id=headers.get('X-Consumer-ID', None),
                    x_consumer_custom_id=headers.get(
                        'X-Consumer-Custom-ID', None),
                    x_consumer_username=headers.get(
                        'X-Consumer-Username', None),
                    x_authenticated_scope=headers.get(
                        'X-Authenticated-Scope', None),
                    x_authenticated_userid=headers.get(
                        'X-Authenticated-Userid', None),
                )
                
            request.client = client
