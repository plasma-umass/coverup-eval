# file typesystem/json_schema.py:352-355
# lines [352, 353, 354, 355]
# branches []

import pytest
from typesystem import Schema, Field
from typesystem.json_schema import from_json_schema, SchemaDefinitions, NO_DEFAULT

# Assuming the existence of a `from_json_schema` function and `SchemaDefinitions` class
# in the `typesystem.json_schema` module, as well as an `AllOf` field class within `typesystem`.

class AllOf(Field):
    def __init__(self, all_of, default=NO_DEFAULT, **kwargs):
        self.all_of = all_of
        self.default = default
        super().__init__(**kwargs)

def all_of_from_json_schema(data: dict, definitions: SchemaDefinitions) -> Field:
    all_of = [from_json_schema(item, definitions=definitions) for item in data["allOf"]]
    kwargs = {"all_of": all_of, "default": data.get("default", NO_DEFAULT)}
    return AllOf(**kwargs)

@pytest.fixture
def schema_definitions():
    return SchemaDefinitions()

@pytest.fixture
def all_of_schema_data():
    return {
        "allOf": [
            {"type": "string"},
            {"minLength": 2}
        ],
        "default": "default_value"
    }

@pytest.fixture
def all_of_schema_data_without_default():
    return {
        "allOf": [
            {"type": "string"},
            {"minLength": 2}
        ]
    }

def test_all_of_from_json_schema_with_default(schema_definitions, all_of_schema_data):
    field = all_of_from_json_schema(all_of_schema_data, schema_definitions)
    assert isinstance(field, AllOf)
    assert field.default == "default_value"
    assert len(field.all_of) == 2

def test_all_of_from_json_schema_without_default(schema_definitions, all_of_schema_data_without_default):
    field = all_of_from_json_schema(all_of_schema_data_without_default, schema_definitions)
    assert isinstance(field, AllOf)
    assert field.default is NO_DEFAULT
    assert len(field.all_of) == 2
