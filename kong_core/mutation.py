from graphene_django.rest_framework.mutation import SerializerMutation, SerializerMutationOptions, fields_for_serializer
from graphene.types import Field, InputField
from graphql_relay.node.node import from_global_id, to_global_id
from graphene.types.objecttype import yank_fields_from_attrs
from .utils import nested_dict


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
        # capturar todos os ids em strings e converter para numerico
        def convert_hash_id_to_plain_id(key, value):
            search_key = 'id'
            if isinstance(value[key], str) and search_key.upper() in value[key].upper():
                try:
                    plain_id = from_global_id(value.get(key))[1]
                    value[key] = plain_id
                except Exception as e:
                    print(e)
                    pass

        nested_dict(input, convert_hash_id_to_plain_id)

        # if 'id' in input:
        # plain_id = from_global_id(input.get(key))[1]
        # input[key] = plain_id

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
