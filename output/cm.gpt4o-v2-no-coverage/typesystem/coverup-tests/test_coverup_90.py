# file: typesystem/json_schema.py:376-394
# asked: {"lines": [377, 378, 379, 380, 381, 383, 384, 385, 386, 388, 389, 390, 391, 392, 394], "branches": []}
# gained: {"lines": [377, 378, 379, 380, 381, 383, 384, 385, 386, 388, 389, 390, 391, 392, 394], "branches": []}

import pytest
from typesystem.composites import IfThenElse
from typesystem.fields import NO_DEFAULT, Field, Const, Any
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import if_then_else_from_json_schema
from typesystem.json_schema import from_json_schema

def test_if_then_else_from_json_schema_then_else():
    data = {
        "if": {"const": 1},
        "then": {"const": 2},
        "else": {"const": 3},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Const)
    assert result.if_clause.const == 1
    assert isinstance(result.then_clause, Const)
    assert result.then_clause.const == 2
    assert isinstance(result.else_clause, Const)
    assert result.else_clause.const == 3
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_no_then():
    data = {
        "if": {"const": 1},
        "else": {"const": 3},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Const)
    assert result.if_clause.const == 1
    assert isinstance(result.then_clause, Any)
    assert isinstance(result.else_clause, Const)
    assert result.else_clause.const == 3
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_no_else():
    data = {
        "if": {"const": 1},
        "then": {"const": 2},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Const)
    assert result.if_clause.const == 1
    assert isinstance(result.then_clause, Const)
    assert result.then_clause.const == 2
    assert isinstance(result.else_clause, Any)
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_no_then_no_else():
    data = {
        "if": {"const": 1},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()
    result = if_then_else_from_json_schema(data, definitions)
    
    assert isinstance(result, IfThenElse)
    assert isinstance(result.if_clause, Const)
    assert result.if_clause.const == 1
    assert isinstance(result.then_clause, Any)
    assert isinstance(result.else_clause, Any)
    assert result.default == "default_value"
