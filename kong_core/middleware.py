from django.utils.deprecation import MiddlewareMixin
from .models import Client
from django.contrib.auth import get_user_model


class KongClientMiddleware(MiddlewareMixin):
    def process_request(self, request):
        headers = request.headers
        user = None

        if headers is not None and headers.get('X-Consumer-ID', False):

            try:
                client = Client.objects.get(pk=headers.get('X-Consumer-ID'))
            except Client.DoesNotExist:
                client = None

            if client is None:
                client = Client(
                    x_consumer_id=headers.get('X-Consumer-ID', None),
                    x_consumer_custom_id=headers.get(
                        'X-Consumer-Custom-ID', None),
                    x_consumer_username=headers.get(
                        'X-Consumer-Username', None),
                    x_authenticated_scope=headers.get(
                        'X-Authenticated-Scope', None),
                    x_authenticated_userid=headers.get(
                        'X-Authenticated-Userid', None)
                )

                client.save()
            try:
                user = get_user_model().objects.get(pk=client.x_authenticated_userid)
            except get_user_model().DoesNotExist:
                user = None

            request.client = client
            request.user = user
