from graphene_django.fields import DjangoConnectionField
from graphene_permissions.mixins import AuthNode, AuthMutation, AuthFilter
from graphene_permissions.permissions import AllowAny
from .errors import PermissionDenied


class UserAuthNode(AuthNode):
    permission_users = (AllowAny,)

    @classmethod
    def get_node(cls, info, id):
        object_instance = super(UserAuthNode, cls).get_node(info, id)

        if object_instance is not None and any((perm.has_node_permission(info, id) for perm in cls.permission_users)):
            return object_instance
        raise PermissionDenied()


class UserAuthFilter(AuthFilter):
    permission_users = (AllowAny,)

    @classmethod
    def has_permission(cls, info):
        object_instance = super(UserAuthFilter, cls).has_permission(info)

        if object_instance is not None and any((perm.has_filter_permission(info) for perm in cls.permission_users)):
            return object_instance
        raise PermissionDenied()


class UserAuthList(DjangoConnectionField):
    """
    Custom ConnectionField for permission system.
    """
    permission_classes = (AllowAny,)
    permission_users = (AllowAny,)

    @classmethod
    def has_permission(cls, info):
        return all(
            (perm().has_filter_permission(info)
             for perm in cls.permission_classes)
        ) and any((perm.has_filter_permission(info) for perm in cls.permission_users))

    @classmethod
    def connection_resolver(
        cls,
        resolver,
        connection,
        default_manager,
        max_limit,
        enforce_first_or_last,
        root,
        info,
        **args
    ):
        if not cls.has_permission(info):
            raise PermissionDenied()

        return super(UserAuthList, cls).connection_resolver(
            resolver, connection, default_manager, max_limit, enforce_first_or_last,
            root, info, **args,
        )


class UserAuthMutation(AuthMutation):
    permission_users = (AllowAny,)

    @classmethod
    def has_permission(cls, root, info, input):
        return super(UserAuthMutation, cls) and any((perm.has_mutation_permission(root=root, info=info, input=input) for perm in cls.permission_users))
