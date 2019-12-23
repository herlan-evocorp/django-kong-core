from .utils import ChoiceEnum

class GroupEnum(ChoiceEnum):
    INSTALADOR = 'INSTALADOR'
    CLIENTE = 'CLIENTE'
    GESTOR = 'GESTOR'

    DEFAULT = 'DEFAULT'