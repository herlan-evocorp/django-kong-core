import requests
from django.conf import settings
from .utils import get_fields


def get_user_remote(info, titular):
    dicionario = get_fields(info)

    url = "{}/graphql".format(settings.ENTIDADE_URL)

    try:
        data = {
            'query': 'query{getUser(id:"' + str(titular.x_authenticated_userid) + '"){' + ' '.join(dicionario.keys()) + '}}'}
        response = requests.post(url, data=data, headers={}, verify=False)

        return response.json().get('data').get('getUser')
    except Exception as e:
        raise Exception(e)
