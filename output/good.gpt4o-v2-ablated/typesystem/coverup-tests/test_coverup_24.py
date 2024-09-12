# file: typesystem/tokenize/tokenize_yaml.py:112-128
# asked: {"lines": [125, 127, 128], "branches": []}
# gained: {"lines": [125, 127, 128], "branches": []}

import pytest
from typesystem.tokenize.tokenize_yaml import validate_yaml
from typesystem import Field, Schema
import yaml

class MockField(Field):
    def validate(self, value, *, context=None):
        return value, []

class MockSchema(Schema):
    def validate(self, value, *, context=None):
        return value, []

def test_validate_yaml_with_string_content(monkeypatch):
    content = "key: value"
    validator = MockField()

    def mock_tokenize_yaml(content):
        return content

    def mock_validate_with_positions(token, validator):
        return token, []

    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.tokenize_yaml', mock_tokenize_yaml)
    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.validate_with_positions', mock_validate_with_positions)

    value, error_messages = validate_yaml(content, validator)
    assert value == content
    assert error_messages == []

def test_validate_yaml_with_bytes_content(monkeypatch):
    content = b"key: value"
    validator = MockSchema

    def mock_tokenize_yaml(content):
        return content.decode()

    def mock_validate_with_positions(token, validator):
        return token, []

    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.tokenize_yaml', mock_tokenize_yaml)
    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.validate_with_positions', mock_validate_with_positions)

    value, error_messages = validate_yaml(content, validator)
    assert value == content.decode()
    assert error_messages == []

def test_validate_yaml_with_invalid_content(monkeypatch):
    content = "key: value: invalid"
    validator = MockField()

    def mock_tokenize_yaml(content):
        raise yaml.YAMLError("Invalid YAML")

    def mock_validate_with_positions(token, validator):
        return token, ["Invalid YAML"]

    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.tokenize_yaml', mock_tokenize_yaml)
    monkeypatch.setattr('typesystem.tokenize.tokenize_yaml.validate_with_positions', mock_validate_with_positions)

    with pytest.raises(yaml.YAMLError):
        validate_yaml(content, validator)
