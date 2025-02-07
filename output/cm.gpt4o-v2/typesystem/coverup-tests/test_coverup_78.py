# file: typesystem/json_schema.py:352-355
# asked: {"lines": [352, 353, 354, 355], "branches": []}
# gained: {"lines": [352, 353, 354, 355], "branches": []}

import pytest
from typesystem.json_schema import all_of_from_json_schema
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import Field, NO_DEFAULT
from typesystem.composites import AllOf

def test_all_of_from_json_schema():
    data = {
        "allOf": [
            {"type": "string"},
            {"type": "number"}
        ],
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    
    result = all_of_from_json_schema(data, definitions)
    
    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert result.default == "default_value"

def test_all_of_from_json_schema_no_default():
    data = {
        "allOf": [
            {"type": "string"},
            {"type": "number"}
        ]
    }
    definitions = SchemaDefinitions()
    
    result = all_of_from_json_schema(data, definitions)
    
    assert isinstance(result, AllOf)
    assert len(result.all_of) == 2
    assert not hasattr(result, 'default')
