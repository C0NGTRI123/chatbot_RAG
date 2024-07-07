import pydantic  # pydantic: ignore
import json
from typing import TypeVar

PydanticBaseModel = pydantic.BaseModel

TBaseModel = TypeVar("TBaseModel", bound=PydanticBaseModel)


class PydanticOutputParser:
    def __init__(self, pydantic_object: PydanticBaseModel):
        self.pydantic_object: TBaseModel = pydantic_object

    def get_format_instructions(self) -> str:
        schema = {k: v for k, v in self.pydantic_object.schema().items()}
        reduced_schema = schema
        if "title" in reduced_schema:
            del reduced_schema["title"]
        if "type" in reduced_schema:
            del reduced_schema["type"]
        schema_str = json.dumps(reduced_schema)
        return PYDANTIC_FORMAT_INSTRUCTIONS.format(schema=schema_str)


# PYDANTIC_FORMAT_INSTRUCTIONS = """La salida debe formatearse como una instancia JSON que se ajuste al siguiente esquema JSON.
#
# A titre d'exemple, pour le schéma {{"properties": {{"foo": {{"title": "Foo", "description": "une liste de chaînes", "type": "array", "items ": {{"type": "string"}}}}}}, "obligatoire": ["foo"]}}
# L'objet {{"foo": ["bar", "baz"]}} est une instance bien formatée du schéma. L'objet {{"properties": {{"foo": ["bar", "baz"]}}}} n'est pas bien formaté.
#
# A continuación, se presenta el esquema de salida:
# ```
# {schemas}
# ```"""  # noqa: E501

PYDANTIC_FORMAT_INSTRUCTIONS = """The output should be formatted as a JSON instance that conforms to the JSON schemas below.

As an example, for the schemas {{"properties": {{"foo": {{"title": "Foo", "description": "a list of strings", "type": "array", "items": {{"type": "string"}}}}}}, "required": ["foo"]}}
the object {{"foo": ["bar", "baz"]}} is a well-formatted instance of the schemas. The object {{"properties": {{"foo": ["bar", "baz"]}}}} is not well-formatted.

Here is the output schemas:
```
{schemas}
```"""  # noqa: E501


