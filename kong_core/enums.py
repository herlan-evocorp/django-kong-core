from .utils import ChoiceEnum

class TipoUsuario(ChoiceEnum):
    INSTALADOR = 'INSTALADOR'
    CLIENTE = 'CLIENTE'
    GESTOR = 'GESTOR'

    DEFAULT = 'DEFAULT'