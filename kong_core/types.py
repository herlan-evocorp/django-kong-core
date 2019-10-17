import graphene
from kong_core.connections import TotalItemsConnection


class UserRemoteType(graphene.ObjectType):
    id = graphene.ID()
    email = graphene.String()
    full_name = graphene.String()
    cpf = graphene.String()
    telefone = graphene.String()
    username = graphene.String()
    first_name = graphene.String()
    last_name = graphene.String()
    data_nascimento = graphene.String()
    cep = graphene.String()
    rua = graphene.String()
    numero = graphene.String()
    bairro = graphene.String()
    complemento = graphene.String()
    cidade_name = graphene.String()
    cidade_estado_name = graphene.String()
    tipo_usuario = graphene.String()

    class Meta:
        fields = ['id', 'email', 'full_name', 'cpf', 'telefone', 'username',
                  'first_name', 'last_name' 'data_nascimento', 'cep', 'rua',
                  'numero', 'bairro', 'complemento', 'cidade_name', 'cidade_estado_name',
                  'tipo_usuario', ]
        connection_class = TotalItemsConnection
        use_connection = True
