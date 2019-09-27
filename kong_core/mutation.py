from graphene_django.rest_framework.mutation import SerializerMutation
from graphql_relay.node.node import from_global_id

class RNASerializerMutation(SerializerMutation):
    class Meta:
        abstract = True

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        if 'id' in input:
            plain_id = from_global_id(input.get('id'))[1]
            input['id'] = plain_id
        return super(RNASerializerMutation, cls).mutate_and_get_payload(root, info, **input)