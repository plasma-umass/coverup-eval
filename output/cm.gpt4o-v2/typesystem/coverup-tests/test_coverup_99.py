# file: typesystem/json_schema.py:110-147
# asked: {"lines": [114, 117, 118, 119, 120, 123, 129, 131, 133, 135, 137, 139, 141, 145, 146, 147], "branches": [[113, 114], [116, 117], [118, 119], [118, 122], [122, 123], [126, 128], [128, 129], [130, 131], [132, 133], [134, 135], [136, 137], [138, 139], [140, 141], [143, 145], [145, 146], [145, 147]]}
# gained: {"lines": [114, 117, 118, 123, 129, 131, 133, 135, 137, 139, 141, 145, 147], "branches": [[113, 114], [116, 117], [118, 122], [122, 123], [126, 128], [128, 129], [130, 131], [132, 133], [134, 135], [136, 137], [138, 139], [140, 141], [143, 145], [145, 147]]}

import pytest
from typesystem.json_schema import from_json_schema
from typesystem.schemas import SchemaDefinitions
from typesystem.fields import Any, Field
from typesystem.composites import AllOf, NeverMatch

def test_from_json_schema_boolean_true():
    schema = True
    field = from_json_schema(schema)
    assert isinstance(field, Any)

def test_from_json_schema_boolean_false():
    schema = False
    field = from_json_schema(schema)
    assert isinstance(field, NeverMatch)

def test_from_json_schema_with_definitions(monkeypatch):
    schema = {
        "definitions": {
            "A": {"type": "string"},
            "B": {"type": "number"}
        }
    }
    definitions = SchemaDefinitions()
    monkeypatch.setattr(definitions, "__setitem__", lambda key, value: None)
    from_json_schema(schema, definitions=definitions)
    assert True  # If no exception, the test passes

def test_from_json_schema_with_ref(monkeypatch):
    schema = {"$ref": "#/definitions/A"}
    definitions = SchemaDefinitions()
    monkeypatch.setattr(definitions, "__getitem__", lambda key: Any())
    field = from_json_schema(schema, definitions=definitions)
    assert isinstance(field, Field)

def test_from_json_schema_with_type_constraint(monkeypatch):
    schema = {"type": "string"}
    monkeypatch.setattr("typesystem.json_schema.TYPE_CONSTRAINTS", ["type"])
    field = from_json_schema(schema)
    assert isinstance(field, Field)

def test_from_json_schema_with_enum(monkeypatch):
    schema = {"enum": ["A", "B", "C"]}
    monkeypatch.setattr("typesystem.json_schema.enum_from_json_schema", lambda data, definitions: Any())
    field = from_json_schema(schema)
    assert isinstance(field, Field)

def test_from_json_schema_with_const(monkeypatch):
    schema = {"const": "A"}
    monkeypatch.setattr("typesystem.json_schema.const_from_json_schema", lambda data, definitions: Any())
    field = from_json_schema(schema)
    assert isinstance(field, Field)

def test_from_json_schema_with_allOf(monkeypatch):
    schema = {"allOf": [{"type": "string"}, {"type": "number"}]}
    monkeypatch.setattr("typesystem.json_schema.all_of_from_json_schema", lambda data, definitions: AllOf([Any(), Any()]))
    field = from_json_schema(schema)
    assert isinstance(field, AllOf)

def test_from_json_schema_with_anyOf(monkeypatch):
    schema = {"anyOf": [{"type": "string"}, {"type": "number"}]}
    monkeypatch.setattr("typesystem.json_schema.any_of_from_json_schema", lambda data, definitions: Any())
    field = from_json_schema(schema)
    assert isinstance(field, Field)

def test_from_json_schema_with_oneOf(monkeypatch):
    schema = {"oneOf": [{"type": "string"}, {"type": "number"}]}
    monkeypatch.setattr("typesystem.json_schema.one_of_from_json_schema", lambda data, definitions: Any())
    field = from_json_schema(schema)
    assert isinstance(field, Field)

def test_from_json_schema_with_not(monkeypatch):
    schema = {"not": {"type": "string"}}
    monkeypatch.setattr("typesystem.json_schema.not_from_json_schema", lambda data, definitions: Any())
    field = from_json_schema(schema)
    assert isinstance(field, Field)

def test_from_json_schema_with_if_then_else(monkeypatch):
    schema = {"if": {"type": "string"}, "then": {"type": "number"}, "else": {"type": "boolean"}}
    monkeypatch.setattr("typesystem.json_schema.if_then_else_from_json_schema", lambda data, definitions: Any())
    field = from_json_schema(schema)
    assert isinstance(field, Field)
