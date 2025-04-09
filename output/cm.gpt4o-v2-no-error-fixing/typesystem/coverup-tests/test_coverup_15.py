# file: typesystem/json_schema.py:376-394
# asked: {"lines": [376, 377, 378, 379, 380, 381, 383, 384, 385, 386, 388, 389, 390, 391, 392, 394], "branches": []}
# gained: {"lines": [376, 377, 378, 379, 380, 381, 383, 384, 385, 386, 388, 389, 390, 391, 392, 394], "branches": []}

import pytest
from typesystem.json_schema import if_then_else_from_json_schema
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import Any, Field
from typesystem.composites import IfThenElse

def test_if_then_else_from_json_schema_with_then_and_else():
    data = {
        "if": {"type": "string"},
        "then": {"type": "number"},
        "else": {"type": "boolean"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Field)
    assert isinstance(result.then_clause, Field)
    assert isinstance(result.else_clause, Field)
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_with_then_only():
    data = {
        "if": {"type": "string"},
        "then": {"type": "number"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Field)
    assert isinstance(result.then_clause, Field)
    assert isinstance(result.else_clause, Any)
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_with_else_only():
    data = {
        "if": {"type": "string"},
        "else": {"type": "boolean"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Field)
    assert isinstance(result.then_clause, Any)
    assert isinstance(result.else_clause, Field)
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_with_no_then_or_else():
    data = {
        "if": {"type": "string"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Field)
    assert isinstance(result.then_clause, Any)
    assert isinstance(result.else_clause, Any)
    assert result.default == "default_value"
