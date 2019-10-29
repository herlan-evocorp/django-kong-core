from django.utils.translation import ugettext_lazy as _
from graphql import GraphQLError as BaseGraphQLError


class GraphQLError(BaseGraphQLError):
    message = _("Ocorreu um erro")

    def __init__(self, message=None, *args, **kwags):
        if message is None:
            message = self.message
        super(GraphQLError, self).__init__(message, *args, **kwags)


class PermissionDenied(GraphQLError):
    message = _("Você não tem permissão para isso!")
    
    
class HasRelationsException(Exception):
    def __init__(self, object_relation, object_related):
        self.object_relation = object_relation
        self.object_related = object_related
    def __str__(self):
        return "Este(a) {} está vinculado a um(a) {}".format(self.object_relation, self.object_related)
