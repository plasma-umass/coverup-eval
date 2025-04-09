# file typesystem/json_schema.py:376-394
# lines [377, 378, 379, 380, 381, 383, 384, 385, 386, 388, 389, 390, 391, 392, 394]
# branches []

import pytest
from typesystem.fields import Field, Any
from typesystem.json_schema import from_json_schema, IfThenElse, SchemaDefinitions

@pytest.fixture
def schema_definitions():
    return SchemaDefinitions()

@pytest.fixture
def if_then_else_schema():
    return {
        "if": {
            "type": "object",
            "properties": {
                "propertyName": {"type": "string"}
            },
            "required": ["propertyName"]
        },
        "then": {
            "type": "object",
            "properties": {
                "thenProperty": {"type": "number"}
            }
        },
        "else": {
            "type": "object",
            "properties": {
                "elseProperty": {"type": "boolean"}
            }
        }
    }

def test_if_then_else_from_json_schema(schema_definitions, if_then_else_schema):
    field = from_json_schema(if_then_else_schema, definitions=schema_definitions)
    assert isinstance(field, IfThenElse)
    assert isinstance(field.if_clause, Field)
    assert isinstance(field.then_clause, Field)
    assert isinstance(field.else_clause, Field)

def test_if_then_without_else_from_json_schema(schema_definitions):
    schema = {
        "if": {
            "type": "object",
            "properties": {
                "propertyName": {"type": "string"}
            },
            "required": ["propertyName"]
        },
        "then": {
            "type": "object",
            "properties": {
                "thenProperty": {"type": "number"}
            }
        }
    }
    field = from_json_schema(schema, definitions=schema_definitions)
    assert isinstance(field, IfThenElse)
    assert isinstance(field.if_clause, Field)
    assert isinstance(field.then_clause, Field)
    assert isinstance(field.else_clause, Any)

def test_if_else_without_then_from_json_schema(schema_definitions):
    schema = {
        "if": {
            "type": "object",
            "properties": {
                "propertyName": {"type": "string"}
            },
            "required": ["propertyName"]
        },
        "else": {
            "type": "object",
            "properties": {
                "elseProperty": {"type": "boolean"}
            }
        }
    }
    field = from_json_schema(schema, definitions=schema_definitions)
    assert isinstance(field, IfThenElse)
    assert isinstance(field.if_clause, Field)
    assert isinstance(field.then_clause, Any)
    assert isinstance(field.else_clause, Field)
