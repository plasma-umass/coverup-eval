# file: f093/__init__.py:1-6
# asked: {"lines": [1, 3, 4, 5, 6], "branches": []}
# gained: {"lines": [1, 3, 4, 5, 6], "branches": []}

import pytest
from f093 import encode

def test_encode_all_vowels():
    message = "aeiouAEIOU"
    expected = "CGKQWcgkqw"
    assert encode(message) == expected

def test_encode_mixed_case():
    message = "Hello World"
    expected = "hGLLQ wQRLD"
    assert encode(message) == expected

def test_encode_no_vowels():
    message = "bcdfg"
    expected = "BCDFG"
    assert encode(message) == expected

def test_encode_empty_string():
    message = ""
    expected = ""
    assert encode(message) == expected
