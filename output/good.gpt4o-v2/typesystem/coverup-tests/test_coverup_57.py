# file: typesystem/fields.py:677-679
# asked: {"lines": [677, 678, 679], "branches": []}
# gained: {"lines": [677, 678, 679], "branches": []}

import pytest
from typesystem.fields import Text

def test_text_initialization():
    # Test initialization with no additional arguments
    text_field = Text()
    assert text_field.format == "text"

    # Test initialization with additional arguments
    text_field = Text(max_length=100, allow_blank=True)
    assert text_field.format == "text"
    assert text_field.max_length == 100
    assert text_field.allow_blank is True

    # Test initialization with pattern
    text_field = Text(pattern=r"^\w+$")
    assert text_field.format == "text"
    assert text_field.pattern == r"^\w+$"
    assert text_field.pattern_regex.match("valid_text")

    # Test initialization with min_length
    text_field = Text(min_length=5)
    assert text_field.format == "text"
    assert text_field.min_length == 5

    # Test initialization with trim_whitespace
    text_field = Text(trim_whitespace=False)
    assert text_field.format == "text"
    assert text_field.trim_whitespace is False
