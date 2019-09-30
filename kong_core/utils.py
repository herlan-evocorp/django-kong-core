from enum import Enum


def nested_dict(d, f):
    for k, v in d.items():
        if isinstance(v, dict):
            nested_dict(v, f)
        else:
            f(k, v)


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
