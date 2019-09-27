from graphene import relay
from graphene import Int

class TotalItemsConnection(relay.Connection):
    class Meta:
        abstract = True

    total = Int()

    def resolve_total(self, info, **kwargs):
        return self.iterable.count()