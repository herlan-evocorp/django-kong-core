from graphene_permissions.permissions import AllowAny
from .enums import TipoUsuario


class DennyAny(AllowAny):
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
        return info.request.client is not None

    @staticmethod
    def has_mutation_permission(root, info, input):
        return info.request.client is not None

    @staticmethod
    def has_filter_permission(info):
        return info.request.client is not None


# can access node
class AllowClientNode(DennyAny):
    @staticmethod
    def has_node_permission(info, id):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.CLIENTE.name
        return False


class AllowInstaladorNode(DennyAny):
    @staticmethod
    def has_node_permission(info, id):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.INSTALADOR.name
        return False


class AllowGestorNode(DennyAny):
    @staticmethod
    def has_node_permission(info, id):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.GESTOR.name
        return False


# can make mutation
class AllowClientMutation(DennyAny):
    @staticmethod
    def has_mutation_permission(root, info, input):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.CLIENTE.name
        return False


class AllowInstaladorMutation(DennyAny):
    @staticmethod
    def has_mutation_permission(root, info, input):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.INSTALADOR.name
        return False


class AllowGestorMutation(DennyAny):
    @staticmethod
    def has_mutation_permission(root, info, input):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.GESTOR.name
        return False


# can filter
class AllowClientFilter(DennyAny):
    @staticmethod
    def has_filter_permission(info):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.CLIENTE.name
        return False


class AllowInstaladorFilter(DennyAny):
    @staticmethod
    def has_filter_permission(info):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.INSTALADOR.name
        return False


class AllowGestorFilter(DennyAny):
    @staticmethod
    def has_filter_permission(info):
        if info.request.client is not None:
            info.request.client.user_type == TipoUsuario.GESTOR.name
        return False
