from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-updated_at']


class Client(BaseModel):
    x_consumer_id = models.CharField(max_length=256, primary_key=True)
    x_consumer_custom_id = models.CharField(max_length=256, null=True)
    x_consumer_username = models.CharField(max_length=256, null=True)
    x_authenticated_scope = models.CharField(max_length=256, null=True)
    x_authenticated_userid = models.PositiveIntegerField(null=True)
    x_anonymous_consumer = models.BooleanField(default=False)

    def __str__(self):
        return self.x_consumer_id
