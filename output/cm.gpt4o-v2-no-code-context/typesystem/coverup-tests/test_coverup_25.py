# file: typesystem/fields.py:106-141
# asked: {"lines": [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141], "branches": [[124, 125], [124, 127], [133, 134], [133, 136], [136, 137], [136, 140]]}
# gained: {"lines": [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141], "branches": [[124, 125], [124, 127], [133, 134], [133, 136], [136, 137], [136, 140]]}

import pytest
import re
from typesystem.fields import String

def test_string_field_initialization():
    # Test with default parameters
    field = String()
    assert field.allow_blank == False
    assert field.trim_whitespace == True
    assert field.max_length is None
    assert field.min_length is None
    assert field.pattern is None
    assert field.pattern_regex is None
    assert field.format is None

def test_string_field_with_parameters():
    # Test with all parameters
    field = String(
        allow_blank=True,
        trim_whitespace=False,
        max_length=10,
        min_length=5,
        pattern=r'^[a-z]+$',
        format='email'
    )
    assert field.allow_blank == True
    assert field.trim_whitespace == False
    assert field.max_length == 10
    assert field.min_length == 5
    assert field.pattern == r'^[a-z]+$'
    assert field.pattern_regex.pattern == r'^[a-z]+$'
    assert field.format == 'email'

def test_string_field_with_pattern_as_regex():
    # Test with pattern as a compiled regex
    regex = re.compile(r'^[a-z]+$')
    field = String(pattern=regex)
    assert field.pattern == regex.pattern
    assert field.pattern_regex == regex

def test_string_field_allow_blank_with_default(monkeypatch):
    # Test allow_blank with default value
    def mock_has_default(self):
        return False

    monkeypatch.setattr(String, "has_default", mock_has_default)
    field = String(allow_blank=True)
    assert field.allow_blank == True
    assert field.default == ""

def test_string_field_invalid_max_length():
    with pytest.raises(AssertionError):
        String(max_length='invalid')

def test_string_field_invalid_min_length():
    with pytest.raises(AssertionError):
        String(min_length='invalid')

def test_string_field_invalid_pattern():
    with pytest.raises(AssertionError):
        String(pattern=123)

def test_string_field_invalid_format():
    with pytest.raises(AssertionError):
        String(format=123)
