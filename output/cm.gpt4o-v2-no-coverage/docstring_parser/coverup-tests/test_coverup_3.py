# file: docstring_parser/numpydoc.py:27-30
# asked: {"lines": [27, 28, 29, 30], "branches": [[29, 0], [29, 30]]}
# gained: {"lines": [27, 28, 29, 30], "branches": [[29, 0], [29, 30]]}

import pytest
from docstring_parser.numpydoc import _clean_str

def test_clean_str_non_empty():
    result = _clean_str("  some string  ")
    assert result == "some string"

def test_clean_str_empty():
    result = _clean_str("   ")
    assert result is None

def test_clean_str_no_whitespace():
    result = _clean_str("string")
    assert result == "string"
