# file: typesystem/fields.py:692-694
# asked: {"lines": [692, 693, 694], "branches": []}
# gained: {"lines": [692, 693, 694], "branches": []}

import pytest
from typesystem.fields import DateTime

def test_datetime_init():
    # Test initialization with no additional arguments
    dt = DateTime()
    assert dt.format == 'datetime'
    assert dt.allow_blank == False
    assert dt.trim_whitespace == True
    assert dt.max_length is None
    assert dt.min_length is None
    assert dt.pattern is None
    assert dt.pattern_regex is None

    # Test initialization with additional arguments
    dt = DateTime(allow_blank=True, max_length=10, min_length=5, pattern=r'\d{4}-\d{2}-\d{2}')
    assert dt.format == 'datetime'
    assert dt.allow_blank == True
    assert dt.trim_whitespace == True
    assert dt.max_length == 10
    assert dt.min_length == 5
    assert dt.pattern == r'\d{4}-\d{2}-\d{2}'
    assert dt.pattern_regex.pattern == r'\d{4}-\d{2}-\d{2}'
