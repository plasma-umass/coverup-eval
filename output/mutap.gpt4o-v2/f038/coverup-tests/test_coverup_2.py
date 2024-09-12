# file: f038/__init__.py:1-7
# asked: {"lines": [1, 4, 6, 7], "branches": []}
# gained: {"lines": [1, 4, 6, 7], "branches": []}

import pytest
from f038 import encode_cyclic

def test_encode_cyclic_full_groups():
    result = encode_cyclic("abcdef")
    assert result == "bcaefd", f"Expected 'bcaefd' but got {result}"

def test_encode_cyclic_partial_group():
    result = encode_cyclic("abcd")
    assert result == "bcad", f"Expected 'bcad' but got {result}"

def test_encode_cyclic_single_group():
    result = encode_cyclic("abc")
    assert result == "bca", f"Expected 'bca' but got {result}"

def test_encode_cyclic_less_than_group():
    result = encode_cyclic("ab")
    assert result == "ab", f"Expected 'ab' but got {result}"

def test_encode_cyclic_empty_string():
    result = encode_cyclic("")
    assert result == "", f"Expected '' but got {result}"
