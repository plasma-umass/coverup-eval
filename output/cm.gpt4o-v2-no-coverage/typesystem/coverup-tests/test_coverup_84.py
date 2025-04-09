# file: typesystem/json_schema.py:150-171
# asked: {"lines": [157, 158, 159, 161, 163, 166], "branches": [[156, 157], [165, 166]]}
# gained: {"lines": [157, 158, 159, 161, 163, 166], "branches": [[156, 157], [165, 166]]}

import pytest
from typesystem.composites import NeverMatch
from typesystem.fields import Const, Field, Union
from typesystem.schemas import SchemaDefinitions
from typesystem.json_schema import type_from_json_schema

def test_type_from_json_schema_union(monkeypatch):
    def mock_get_valid_types(data):
        return ({"string", "number"}, False)
    
    def mock_from_json_schema_type(data, type_string, allow_null, definitions):
        return Field()
    
    monkeypatch.setattr("typesystem.json_schema.get_valid_types", mock_get_valid_types)
    monkeypatch.setattr("typesystem.json_schema.from_json_schema_type", mock_from_json_schema_type)
    
    data = {"type": ["string", "number"]}
    definitions = SchemaDefinitions()
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, Union)
    assert len(result.any_of) == 2

def test_type_from_json_schema_const(monkeypatch):
    def mock_get_valid_types(data):
        return (set(), True)
    
    monkeypatch.setattr("typesystem.json_schema.get_valid_types", mock_get_valid_types)
    
    data = {"type": []}
    definitions = SchemaDefinitions()
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, Const)
    assert result.const is None

def test_type_from_json_schema_nevermatch(monkeypatch):
    def mock_get_valid_types(data):
        return (set(), False)
    
    monkeypatch.setattr("typesystem.json_schema.get_valid_types", mock_get_valid_types)
    
    data = {"type": []}
    definitions = SchemaDefinitions()
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, NeverMatch)

def test_type_from_json_schema_single_type(monkeypatch):
    def mock_get_valid_types(data):
        return ({"string"}, False)
    
    def mock_from_json_schema_type(data, type_string, allow_null, definitions):
        return Field()
    
    monkeypatch.setattr("typesystem.json_schema.get_valid_types", mock_get_valid_types)
    monkeypatch.setattr("typesystem.json_schema.from_json_schema_type", mock_from_json_schema_type)
    
    data = {"type": "string"}
    definitions = SchemaDefinitions()
    result = type_from_json_schema(data, definitions)
    
    assert isinstance(result, Field)
