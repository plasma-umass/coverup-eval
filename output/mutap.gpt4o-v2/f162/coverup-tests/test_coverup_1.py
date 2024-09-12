# file: f162/__init__.py:1-4
# asked: {"lines": [1, 3, 4], "branches": []}
# gained: {"lines": [1, 3, 4], "branches": []}

import pytest
from f162 import string_to_md5

def test_string_to_md5_with_text():
    result = string_to_md5("hello")
    assert result == "5d41402abc4b2a76b9719d911017c592"

def test_string_to_md5_with_empty_string():
    result = string_to_md5("")
    assert result is None

def test_string_to_md5_with_none():
    result = string_to_md5(None)
    assert result is None
