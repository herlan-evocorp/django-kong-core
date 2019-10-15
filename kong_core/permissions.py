from graphene_permissions.permissions import AllowAny
from .enums import TipoUsuario


class DenyAny(AllowAny):
    @staticmethod
    def has_node_permission(info, id):
        return False

    @staticmethod
    def has_mutation_permission(root, info, input):
        return False

    @staticmethod
    def has_filter_permission(info):
        return False


class AllowAuthenticated(AllowAny):
    @staticmethod
    def has_node_permission(info, id):
        return info.context.client is not None

    @staticmethod
    def has_mutation_permission(root, info, input):
        return info.context.client is not None

    @staticmethod
    def has_filter_permission(info):
        return info.context.client is not None


# can access node
class AllowClienteNode(DenyAny):
    @staticmethod
    def has_node_permission(info, id):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.CLIENTE.name
        return False


class AllowInstaladorNode(DenyAny):
    @staticmethod
    def has_node_permission(info, id):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.INSTALADOR.name
        return False


class AllowGestorNode(DenyAny):
    @staticmethod
    def has_node_permission(info, id):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.GESTOR.name
        return False


# can make mutation
class AllowClienteMutation(DenyAny):
    @staticmethod
    def has_mutation_permission(root, info, input):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.CLIENTE.name
        return False


class AllowInstaladorMutation(DenyAny):
    @staticmethod
    def has_mutation_permission(root, info, input):
        if info.context.client is not None:
           return info.context.client.user_type == TipoUsuario.INSTALADOR.name
        return False


class AllowGestorMutation(DenyAny):
    @staticmethod
    def has_mutation_permission(root, info, input):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.GESTOR.name
        return False


# can filter
class AllowClienteFilter(DenyAny):
    @staticmethod
    def has_filter_permission(info):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.CLIENTE.name
        return False


class AllowInstaladorFilter(DenyAny):
    @staticmethod
    def has_filter_permission(info):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.INSTALADOR.name
        return False


class AllowGestorFilter(DenyAny):
    @staticmethod
    def has_filter_permission(info):
        if info.context.client is not None:
            return info.context.client.user_type == TipoUsuario.GESTOR.name
        return False
