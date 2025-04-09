# file: typesystem/tokenize/tokenize_json.py:183-197
# asked: {"lines": [183, 196, 197], "branches": []}
# gained: {"lines": [183, 196, 197], "branches": []}

import pytest
from typesystem.tokenize.tokenize_json import validate_json, Field, Schema

def test_validate_json_with_valid_string(monkeypatch):
    content = '{"key": "value"}'
    validator = Field()

    def mock_tokenize_json(content):
        return {"key": "value"}

    def mock_validate_with_positions(token, validator):
        return (token, [])

    monkeypatch.setattr('typesystem.tokenize.tokenize_json.tokenize_json', mock_tokenize_json)
    monkeypatch.setattr('typesystem.tokenize.tokenize_json.validate_with_positions', mock_validate_with_positions)

    value, errors = validate_json(content, validator)
    assert value == {"key": "value"}
    assert errors == []

def test_validate_json_with_invalid_string(monkeypatch):
    content = '{"key": 123}'
    validator = Field()

    def mock_tokenize_json(content):
        return {"key": 123}

    def mock_validate_with_positions(token, validator):
        return (token, ["Invalid type"])

    monkeypatch.setattr('typesystem.tokenize.tokenize_json.tokenize_json', mock_tokenize_json)
    monkeypatch.setattr('typesystem.tokenize.tokenize_json.validate_with_positions', mock_validate_with_positions)

    value, errors = validate_json(content, validator)
    assert value == {"key": 123}
    assert errors == ["Invalid type"]

def test_validate_json_with_schema(monkeypatch):
    content = '{"key": "value"}'
    class MySchema(Schema):
        fields = {"key": Field()}

    def mock_tokenize_json(content):
        return {"key": "value"}

    def mock_validate_with_positions(token, validator):
        return (token, [])

    monkeypatch.setattr('typesystem.tokenize.tokenize_json.tokenize_json', mock_tokenize_json)
    monkeypatch.setattr('typesystem.tokenize.tokenize_json.validate_with_positions', mock_validate_with_positions)

    value, errors = validate_json(content, MySchema)
    assert value == {"key": "value"}
    assert errors == []
