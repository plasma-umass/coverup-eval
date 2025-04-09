# file: typesystem/fields.py:106-141
# asked: {"lines": [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141], "branches": [[124, 125], [124, 127], [133, 134], [133, 136], [136, 137], [136, 140]]}
# gained: {"lines": [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141], "branches": [[124, 125], [124, 127], [133, 134], [133, 136], [136, 137], [136, 140]]}

import pytest
import re
import typing
from typesystem.fields import String
from typesystem.fields import Field

class MockField(Field):
    def has_default(self):
        return hasattr(self, 'default')

@pytest.fixture
def mock_field():
    return MockField()

def test_string_init_default(mock_field, monkeypatch):
    monkeypatch.setattr('typesystem.fields.Field', MockField)
    field = String(allow_blank=True)
    assert field.default == ""
    assert field.allow_blank is True
    assert field.trim_whitespace is True
    assert field.max_length is None
    assert field.min_length is None
    assert field.pattern is None
    assert field.pattern_regex is None
    assert field.format is None

def test_string_init_with_params(mock_field, monkeypatch):
    monkeypatch.setattr('typesystem.fields.Field', MockField)
    pattern = re.compile(r'\d+')
    field = String(
        allow_blank=False,
        trim_whitespace=False,
        max_length=10,
        min_length=5,
        pattern=pattern,
        format="email"
    )
    assert not hasattr(field, 'default')
    assert field.allow_blank is False
    assert field.trim_whitespace is False
    assert field.max_length == 10
    assert field.min_length == 5
    assert field.pattern == pattern.pattern
    assert field.pattern_regex == pattern
    assert field.format == "email"

def test_string_init_with_string_pattern(mock_field, monkeypatch):
    monkeypatch.setattr('typesystem.fields.Field', MockField)
    pattern = r'\d+'
    field = String(pattern=pattern)
    assert field.pattern == pattern
    assert field.pattern_regex.pattern == pattern

def test_string_init_invalid_max_length(mock_field, monkeypatch):
    monkeypatch.setattr('typesystem.fields.Field', MockField)
    with pytest.raises(AssertionError):
        String(max_length="invalid")

def test_string_init_invalid_min_length(mock_field, monkeypatch):
    monkeypatch.setattr('typesystem.fields.Field', MockField)
    with pytest.raises(AssertionError):
        String(min_length="invalid")

def test_string_init_invalid_pattern(mock_field, monkeypatch):
    monkeypatch.setattr('typesystem.fields.Field', MockField)
    with pytest.raises(AssertionError):
        String(pattern=123)

def test_string_init_invalid_format(mock_field, monkeypatch):
    monkeypatch.setattr('typesystem.fields.Field', MockField)
    with pytest.raises(AssertionError):
        String(format=123)
