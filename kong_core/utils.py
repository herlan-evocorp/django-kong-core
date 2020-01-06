from enum import Enum

class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
    @classmethod
    def to_list(cls):
        return [{'key':i.name, 'value': i.value} for i in cls]

