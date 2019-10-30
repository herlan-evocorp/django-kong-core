from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)

    def has_relationships(self):
        # get all the related object
        relations = []

        for rel in self._meta.get_fields():
            try:
                # check if there is a relationship with at least one related object
                related = rel.related_model.objects.filter(
                    **{rel.field.name: self})
                if related.exists():
                    # if there is return a Tuple
                    relations.append(related)

            except AttributeError:  # an attribute error for field occurs when checking for AutoField
                pass  # just pass as we dont need to check for AutoField

        is_related = len(relations) > 0
        return is_related, relations

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
    user_type = models.CharField(max_length=256, null=True)

    def __str__(self):
        return self.x_consumer_id
