# file: typesystem/fields.py:106-141
# asked: {"lines": [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141], "branches": [[124, 125], [124, 127], [133, 134], [133, 136], [136, 137], [136, 140]]}
# gained: {"lines": [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141], "branches": [[124, 125], [124, 127], [133, 134], [133, 136], [136, 137], [136, 140]]}

import pytest
import re
from typesystem.fields import String, Field

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

    # Test with allow_blank and default not set
    field = String(allow_blank=True)
    assert field.allow_blank == True
    assert field.default == ""

    # Test with max_length and min_length
    field = String(max_length=10, min_length=5)
    assert field.max_length == 10
    assert field.min_length == 5

    # Test with pattern as string
    field = String(pattern="^[a-z]+$")
    assert field.pattern == "^[a-z]+$"
    assert field.pattern_regex == re.compile("^[a-z]+$")

    # Test with pattern as compiled regex
    regex = re.compile("^[a-z]+$")
    field = String(pattern=regex)
    assert field.pattern == regex.pattern
    assert field.pattern_regex == regex

    # Test with format
    field = String(format="email")
    assert field.format == "email"

def test_string_field_assertions():
    with pytest.raises(AssertionError):
        String(max_length="not an int")
    with pytest.raises(AssertionError):
        String(min_length="not an int")
    with pytest.raises(AssertionError):
        String(pattern=123)
    with pytest.raises(AssertionError):
        String(format=123)
