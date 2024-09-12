# file: f089/__init__.py:1-10
# asked: {"lines": [1, 3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}
# gained: {"lines": [1, 3, 4, 5, 6, 7, 9, 10], "branches": [[5, 6], [5, 10], [6, 7], [6, 9]]}

import pytest
from f089.__init__ import encrypt

def test_encrypt_all_lowercase():
    result = encrypt("abc")
    assert result == "efg"

def test_encrypt_with_non_alpha():
    result = encrypt("a1b2c3")
    assert result == "e1f2g3"

def test_encrypt_empty_string():
    result = encrypt("")
    assert result == ""

def test_encrypt_mixed_case():
    result = encrypt("aBc")
    assert result == "eBg"
