# file: typesystem/json_schema.py:370-373
# asked: {"lines": [370, 371, 372, 373], "branches": []}
# gained: {"lines": [370, 371, 372, 373], "branches": []}

import pytest
from typesystem.json_schema import not_from_json_schema, SchemaDefinitions, Field, Not, NO_DEFAULT

def test_not_from_json_schema_with_default(monkeypatch):
    class MockField(Field):
        pass

    class MockNot(Not):
        def __init__(self, negated, default):
            self.negated = negated
            self.default = default

    def mock_from_json_schema(data, definitions):
        return MockField()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)
    monkeypatch.setattr('typesystem.json_schema.Not', MockNot)

    data = {
        "not": {"type": "string"},
        "default": "default_value"
    }
    definitions = SchemaDefinitions()

    result = not_from_json_schema(data, definitions)

    assert isinstance(result, MockNot)
    assert isinstance(result.negated, MockField)
    assert result.default == "default_value"

def test_not_from_json_schema_without_default(monkeypatch):
    class MockField(Field):
        pass

    class MockNot(Not):
        def __init__(self, negated, default):
            self.negated = negated
            self.default = default

    def mock_from_json_schema(data, definitions):
        return MockField()

    monkeypatch.setattr('typesystem.json_schema.from_json_schema', mock_from_json_schema)
    monkeypatch.setattr('typesystem.json_schema.Not', MockNot)

    data = {
        "not": {"type": "string"}
    }
    definitions = SchemaDefinitions()

    result = not_from_json_schema(data, definitions)

    assert isinstance(result, MockNot)
    assert isinstance(result.negated, MockField)
    assert result.default == NO_DEFAULT
