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


class AllowCliente:
    @staticmethod
    def has_node_permission(info, id):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.CLIENTE.name

    @staticmethod
    def has_mutation_permission(root, info, input):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.CLIENTE.name

    @staticmethod
    def has_filter_permission(info):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.CLIENTE.name


class AllowInstalador:
    @staticmethod
    def has_node_permission(info, id):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.INSTALADOR.name

    @staticmethod
    def has_mutation_permission(root, info, input):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.INSTALADOR.name

    @staticmethod
    def has_filter_permission(info):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.INSTALADOR.name


class AllowGestor:
    @staticmethod
    def has_node_permission(info, id):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.GESTOR.name

    @staticmethod
    def has_mutation_permission(root, info, input):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.GESTOR.name

    @staticmethod
    def has_filter_permission(info):
        client = info.context.client
        return client is not None and client.user_type == TipoUsuario.GESTOR.name

    
class IsOwner(AllowCliente):
    @staticmethod
    def has_mutation_permission(root, info, input):
        context_client = info.context.client

        owner = input.pop("owner")
        return context_client.pk == owner.pk
