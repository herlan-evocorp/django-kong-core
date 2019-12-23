from graphene_permissions.permissions import AllowAny
from .enums import GroupEnum
from django.contrib.auth.models import Group

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
        client_group = Group.objects.get(name=GroupEnum.CLIENTE.name) 
        return user is not None and client_group in user.groups.all()

    @staticmethod
    def has_mutation_permission(root, info, input):
        client = info.context.client
        client_group = Group.objects.get(name=GroupEnum.CLIENTE.name) 
        return user is not None and client_group in user.groups.all()

    @staticmethod
    def has_filter_permission(info):
        client = info.context.client
        client_group = Group.objects.get(name=GroupEnum.CLIENTE.name) 
        return user is not None and client_group in user.groups.all()


class AllowInstalador:
    @staticmethod
    def has_node_permission(info, id):
        client = info.context.client
        instalador_group = Group.objects.get(name=GroupEnum.INSTALADOR.name) 
        return user is not None and instalador_group in user.groups.all()

    @staticmethod
    def has_mutation_permission(root, info, input):
        client = info.context.client
        instalador_group = Group.objects.get(name=GroupEnum.INSTALADOR.name) 
        return user is not None and instalador_group in user.groups.all()

    @staticmethod
    def has_filter_permission(info):
        client = info.context.client
        instalador_group = Group.objects.get(name=GroupEnum.INSTALADOR.name) 
        return user is not None and instalador_group in user.groups.all()


class AllowGestor:
    @staticmethod
    def has_node_permission(info, id):
        user = info.context.user 
        return user is not None and user.tipo_usuario == GroupEnum.GESTOR.name

    @staticmethod
    def has_mutation_permission(root, info, input):
        user = info.context.user
        return user is not None and user.tipo_usuario == GroupEnum.GESTOR.name

    @staticmethod
    def has_filter_permission(info):
        user = info.context.user 
        return user is not None and user.tipo_usuario == GroupEnum.GESTOR.name

    
class IsOwner(AllowCliente):
    @staticmethod
    def has_mutation_permission(root, info, input):
        context_client = info.context.client

        owner = input.pop("owner")
        return context_client.pk == owner.pk
