import requests
from django.conf import settings
from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)


def get_user_type(x_authenticated_userid):
    url = "{}/graphql".format(settings.ENTIDADE_URL)

    user_type = ''

    try:
        data = {
            'query': 'query{getUser(id:"' + str(x_authenticated_userid) + '"){ tipoUsuario }}'}
        response = requests.post(url, data=data, headers={}, verify=False)
        user_type = response.json()['data']['getUser']['tipoUsuario']
    except Exception as e:
        pass

    return user_type