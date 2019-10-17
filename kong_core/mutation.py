import graphene
from django.utils.translation import ugettext_lazy as _
from graphene_django.types import ErrorType
from graphene_django.rest_framework.mutation import SerializerMutation, SerializerMutationOptions, fields_for_serializer
from graphene.types import Field, InputField
from graphql_relay.node.node import from_global_id, to_global_id
from graphene.types.objecttype import yank_fields_from_attrs
from .errors import PermissionDenied


def convert_hash_id_to_plain_id(d, search_key):
    '''capturar todos os ids em strings e converter para numerico'''
    for key, value in d.items():
        if isinstance(value, dict):
            convert_hash_id_to_plain_id(d, search_key)
        else:
            if isinstance(value, str) and search_key.upper() in key.upper():
                try:
                    plain_id = from_global_id(value)[1]
                    d[key] = plain_id
                except Exception as e:
                    print(e)


class RNASerializerMutation(SerializerMutation):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(
        cls,
        lookup_field=None,
        serializer_class=None,
        model_class=None,
        model_operations=("create", "update"),
        only_fields=(),
        exclude_fields=(),
        **options
    ):

        if hasattr(cls, 'Type'):
            if not hasattr(cls.Type, 'object_type'):
                raise Exception(
                    'object_type is required for the SerializerMutation `Type` class')

        super(RNASerializerMutation, cls).__init_subclass_with_meta__(
            lookup_field,
            serializer_class,
            model_class,
            model_operations,
            only_fields,
            exclude_fields,
            **options
        )

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        if hasattr(cls, 'has_permission') and callable(getattr(cls, 'has_permission')):
            if not cls.has_permission(root, info, input):
                # errors = ErrorType.from_errors(
                #     {'permission': [_('Você não tem permissão para isso!')]})
                # return cls(errors=errors)
                raise PermissionDenied()

        search_key = 'id'
        convert_hash_id_to_plain_id(input, search_key)
        return super(RNASerializerMutation, cls).mutate_and_get_payload(root, info, **input)

    @classmethod
    def perform_mutate(cls, serializer, info):
        obj = serializer.save()

        kwargs = {}
        for f, field in serializer.fields.items():
            if not field.write_only:
                kwargs[f] = field.get_attribute(obj)
        if hasattr(cls, 'Type'):
            kwargs['id'] = to_global_id(
                cls.Type.object_type._meta.name, obj.id)

        return cls(errors=None, **kwargs)
