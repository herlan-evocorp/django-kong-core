from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    x_consumer_id = serializers.CharField(read_only=True)

    class Meta:
        model = Client
        fields = ['x_consumer_id', 'x_consumer_custom_id',
                  'x_consumer_username', 'x_authenticated_scope',
                  'x_authenticated_userid', 'x_anonymous_consumer']
