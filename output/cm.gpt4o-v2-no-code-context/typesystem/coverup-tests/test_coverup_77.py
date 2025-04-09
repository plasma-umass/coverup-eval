# file: typesystem/json_schema.py:376-394
# asked: {"lines": [377, 378, 379, 380, 381, 383, 384, 385, 386, 388, 389, 390, 391, 392, 394], "branches": []}
# gained: {"lines": [377, 378, 379, 380, 381, 383, 384, 385, 386, 388, 389, 390, 391, 392, 394], "branches": []}

import pytest
from typesystem.json_schema import if_then_else_from_json_schema, SchemaDefinitions, Field, IfThenElse, NO_DEFAULT

def test_if_then_else_from_json_schema_if_then_else(monkeypatch):
    data = {
        "if": {"type": "string"},
        "then": {"type": "number"},
        "else": {"type": "boolean"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    def mock_from_json_schema(data, definitions):
        return Field()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    result = if_then_else_from_json_schema(data, definitions)

    assert isinstance(result, IfThenElse)
    assert result.if_clause is not None
    assert result.then_clause is not None
    assert result.else_clause is not None
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_if_then(monkeypatch):
    data = {
        "if": {"type": "string"},
        "then": {"type": "number"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    def mock_from_json_schema(data, definitions):
        return Field()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    result = if_then_else_from_json_schema(data, definitions)

    assert isinstance(result, IfThenElse)
    assert result.if_clause is not None
    assert result.then_clause is not None
    assert result.else_clause is None or isinstance(result.else_clause, Field)
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_if_else(monkeypatch):
    data = {
        "if": {"type": "string"},
        "else": {"type": "boolean"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    def mock_from_json_schema(data, definitions):
        return Field()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    result = if_then_else_from_json_schema(data, definitions)

    assert isinstance(result, IfThenElse)
    assert result.if_clause is not None
    assert result.then_clause is None or isinstance(result.then_clause, Field)
    assert result.else_clause is not None
    assert result.default == "default_value"

def test_if_then_else_from_json_schema_if_only(monkeypatch):
    data = {
        "if": {"type": "string"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    def mock_from_json_schema(data, definitions):
        return Field()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)

    result = if_then_else_from_json_schema(data, definitions)

    assert isinstance(result, IfThenElse)
    assert result.if_clause is not None
    assert result.then_clause is None or isinstance(result.then_clause, Field)
    assert result.else_clause is None or isinstance(result.else_clause, Field)
    assert result.default == "default_value"
