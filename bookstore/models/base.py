from typing import Type, get_type_hints

from pydantic import BaseModel, Extra


def required(required: list[str]):
    def decorator(cls: Type[BaseModel]):
        nonlocal required
        type_hints = get_type_hints(cls)
        fields = cls.__fields__
        optional = fields.keys() - required
        optional = [fields[field_name] for field_name in optional]
        required = [fields[field_name] for field_name in required]
        for field in optional:
            field.required = False
            cls.__annotations__[field.name] = type_hints[field.name] | None
        for field in required:
            field.required = True
        return cls

    return decorator


def to_camelcase(string: str) -> str:
    words = string.split("_")
    for idx, word in enumerate(words[1:], 1):
        words[idx] = word.capitalize()
    return "".join(words)


class CamelCaseModel(BaseModel):
    class Config:
        extra = Extra.forbid
        alias_generator = to_camelcase
        allow_population_by_field_name = True

    def json(self, **kwargs):
        if "by_alias" not in kwargs:
            kwargs["by_alias"] = True
        return super().dict(**kwargs)

    # def dict(self, **kwargs):
    #     if "by_alias" not in kwargs:
    #         kwargs["by_alias"] = True
    #     return super().dict(**kwargs)
