from .utils import ChoiceEnum

class GroupEnum(ChoiceEnum):
    INSTALADOR = 'INSTALADOR'
    COMERCIAL = 'COMERCIAL'
    CLIENTE = 'CLIENTE'
    GESTOR = 'GESTOR'
    DEFAULT = 'DEFAULT'