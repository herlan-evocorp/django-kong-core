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


class UserAuthMutation(AuthMutation):
    permission_users = (AllowAny,)

    @classmethod
    def has_permission(cls, root, info, input):
        return super(UserAuthMutation, cls) and any((perm.has_filter_permission(info) for perm in cls.permission_users))
