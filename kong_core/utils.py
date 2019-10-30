import requests
from enum import Enum
from django.conf import settings
from graphql.utils.ast_to_dict import ast_to_dict


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
        print(e)

    return user_type


def collect_fields(node, fragments):
    """Recursively collects fields from the AST

    Args:
        node (dict): A node in the AST
        fragments (dict): Fragment definitions

    Returns:
        A dict mapping each field found, along with their sub fields.

        {'name': {},
         'sentimentsPerLanguage': {'id': {},
                                   'name': {},
                                   'totalSentiments': {}},
         'slug': {}}
    """

    field = {}

    if node.get('selection_set'):
        for leaf in node['selection_set']['selections']:
            if leaf['kind'] == 'Field':
                field.update({
                    leaf['name']['value']: collect_fields(leaf, fragments)
                })
            elif leaf['kind'] == 'FragmentSpread':
                field.update(collect_fields(fragments[leaf['name']['value']],
                                            fragments))

    return field


def get_fields(info):
    """A convenience function to call collect_fields with info

    Args:
        info (ResolveInfo)

    Returns:
        dict: Returned from collect_fields
    """

    fragments = {}
    node = ast_to_dict(info.field_asts[0])

    for name, value in info.fragments.items():
        fragments[name] = ast_to_dict(value)

    return collect_fields(node, fragments)
