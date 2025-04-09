# file: typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest
from typesystem.fields import String
from typesystem.schemas import Schema
from typesystem.tokenize.tokenize_yaml import validate_yaml

def test_validate_yaml_with_string(monkeypatch):
    class MockToken:
        def __init__(self, value):
            self.value = value

    def mock_tokenize_yaml(content):
        return MockToken(content)

    def mock_validate_with_positions(token, validator):
        return token.value, []

    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.tokenize_yaml', mock_tokenize_yaml)
    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.validate_with_positions', mock_validate_with_positions)

    content = "key: value"
    validator = String()
    value, errors = validate_yaml(content, validator)

    assert value == content
    assert errors == []

def test_validate_yaml_with_schema(monkeypatch):
    class MockToken:
        def __init__(self, value):
            self.value = value

    def mock_tokenize_yaml(content):
        return MockToken(content)

    def mock_validate_with_positions(token, validator):
        return token.value, []

    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.tokenize_yaml', mock_tokenize_yaml)
    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.validate_with_positions', mock_validate_with_positions)

    class ExampleSchema(Schema):
        key = String()

    content = "key: value"
    validator = ExampleSchema
    value, errors = validate_yaml(content, validator)

    assert value == content
    assert errors == []
