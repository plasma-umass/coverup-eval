# file: typesystem/fields.py:677-679
# asked: {"lines": [677, 678, 679], "branches": []}
# gained: {"lines": [677, 678, 679], "branches": []}

import pytest
from typesystem.fields import Text

def test_text_init():
    # Test with no additional kwargs
    text_field = Text()
    assert text_field.format == "text"
    assert text_field.allow_blank == False
    assert text_field.trim_whitespace == True
    assert text_field.max_length is None
    assert text_field.min_length is None
    assert text_field.pattern is None
    assert text_field.pattern_regex is None

    # Test with additional kwargs
    text_field = Text(allow_blank=True, max_length=100, min_length=10, pattern=r'^[a-z]+$')
    assert text_field.format == "text"
    assert text_field.allow_blank == True
    assert text_field.trim_whitespace == True
    assert text_field.max_length == 100
    assert text_field.min_length == 10
    assert text_field.pattern == r'^[a-z]+$'
    assert text_field.pattern_regex.pattern == r'^[a-z]+$'
