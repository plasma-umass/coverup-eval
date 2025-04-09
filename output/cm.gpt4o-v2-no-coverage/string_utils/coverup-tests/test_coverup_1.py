# file: string_utils/validation.py:83-95
# asked: {"lines": [83, 95], "branches": []}
# gained: {"lines": [83, 95], "branches": []}

import pytest
from string_utils.validation import is_string

def test_is_string_with_string():
    assert is_string('foo') == True

def test_is_string_with_bytes():
    assert is_string(b'foo') == False

def test_is_string_with_non_string():
    assert is_string(123) == False
    assert is_string(12.34) == False
    assert is_string(['foo']) == False
    assert is_string({'foo': 'bar'}) == False
    assert is_string(None) == False
