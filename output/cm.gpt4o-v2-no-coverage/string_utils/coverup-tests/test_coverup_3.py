# file: string_utils/validation.py:141-156
# asked: {"lines": [141, 156], "branches": []}
# gained: {"lines": [141, 156], "branches": []}

import pytest
from string_utils.validation import is_integer

def test_is_integer():
    assert is_integer('42') is True
    assert is_integer('-42') is True
    assert is_integer('+42') is True
    assert is_integer('42.0') is False
    assert is_integer('42e3') is True
    assert is_integer('42.3e3') is False
    assert is_integer('abc') is False
    assert is_integer('') is False
    assert is_integer(' ') is False
    assert is_integer('42 ') is False
    assert is_integer(' 42') is False
