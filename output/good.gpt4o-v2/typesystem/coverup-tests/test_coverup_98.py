# file: typesystem/json_schema.py:199-331
# asked: {"lines": [304], "branches": [[303, 304]]}
# gained: {"lines": [304], "branches": [[303, 304]]}

import pytest
from typesystem.json_schema import from_json_schema_type, from_json_schema
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import Object, Field

def test_from_json_schema_type_object_with_additional_properties_bool():
    data = {
        "type": "object",
        "additionalProperties": True
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "object", allow_null=False, definitions=definitions)
    
    assert isinstance(field, Object)
    assert field.additional_properties is True

def test_from_json_schema_type_object_with_additional_properties_schema():
    data = {
        "type": "object",
        "additionalProperties": {"type": "string"}
    }
    definitions = SchemaDefinitions()
    field = from_json_schema_type(data, "object", allow_null=False, definitions=definitions)
    
    assert isinstance(field, Object)
    assert isinstance(field.additional_properties, Field)
    assert field.additional_properties.__class__.__name__ == "String"
