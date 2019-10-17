import graphene
from kong_core.connections import TotalItemsConnection


class UserRemoteType(graphene.ObjectType):
    id = graphene.ID()
    email = graphene.String()
    fullName = graphene.String()
    cpf = graphene.String()
    telefone = graphene.String()
    username = graphene.String()
    firstName = graphene.String()
    lastName = graphene.String()
    data_nascimento = graphene.String()
    cep = graphene.String()
    rua = graphene.String()
    numero = graphene.String()
    bairro = graphene.String()
    complemento = graphene.String()
    cidadeName = graphene.String()
    cidadeEstadoName = graphene.String()
    tipoUsuario = graphene.String()

    class Meta:
        fields = ['id', 'email', 'fullName', 'cpf', 'telefone', 'username',
                  'firstName', 'lastName' 'data_nascimento', 'cep', 'rua',
                  'numero', 'bairro', 'complemento', 'cidadeName', 'cidadeEstadoName',
                  'tipoUsuario', ]
        connection_class = TotalItemsConnection
        use_connection = True
