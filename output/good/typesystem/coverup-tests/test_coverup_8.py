# file typesystem/fields.py:106-141
# lines [106, 109, 110, 111, 112, 113, 114, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 138, 140, 141]
# branches ['124->125', '124->127', '133->134', '133->136', '136->137', '136->140']

import pytest
import re
import typing
from typesystem.fields import String

def test_string_field_initialization():
    # Test with all parameters provided
    pattern = re.compile(r'^[a-zA-Z]+$')
    string_field = String(
        allow_blank=True,
        trim_whitespace=False,
        max_length=10,
        min_length=2,
        pattern=pattern,
        format='email'
    )

    assert string_field.allow_blank is True
    assert string_field.trim_whitespace is False
    assert string_field.max_length == 10
    assert string_field.min_length == 2
    assert string_field.pattern == pattern.pattern
    assert string_field.pattern_regex == pattern
    assert string_field.format == 'email'

    # Test with string pattern
    string_field = String(pattern='^[a-zA-Z]+$')
    assert string_field.pattern == '^[a-zA-Z]+$'
    assert string_field.pattern_regex.match('abc')
    assert not string_field.pattern_regex.match('123')

    # Test with default value for allow_blank
    string_field = String()
    assert string_field.allow_blank is False

    # Test with allow_blank and no default
    string_field = String(allow_blank=True)
    assert string_field.allow_blank is True
    assert string_field.default == ""

    # Test with incorrect types for max_length, min_length, pattern, and format
    with pytest.raises(AssertionError):
        String(max_length='not_an_int')
    with pytest.raises(AssertionError):
        String(min_length='not_an_int')
    with pytest.raises(AssertionError):
        String(pattern=123)
    with pytest.raises(AssertionError):
        String(format=123)

    # Clean up after the test
    del string_field
