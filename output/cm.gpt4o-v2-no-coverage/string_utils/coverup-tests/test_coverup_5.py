# file: string_utils/validation.py:98-113
# asked: {"lines": [98, 113], "branches": []}
# gained: {"lines": [98, 113], "branches": []}

import pytest
from string_utils.validation import is_full_string

def test_is_full_string_with_none():
    assert not is_full_string(None)

def test_is_full_string_with_empty_string():
    assert not is_full_string('')

def test_is_full_string_with_space_string():
    assert not is_full_string(' ')

def test_is_full_string_with_non_empty_string():
    assert is_full_string('hello')

def test_is_full_string_with_non_string():
    assert not is_full_string(123)
    assert not is_full_string([])
    assert not is_full_string({})
    assert not is_full_string(set())
