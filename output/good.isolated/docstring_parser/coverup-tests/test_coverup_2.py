# file docstring_parser/numpydoc.py:27-30
# lines [27, 28, 29, 30]
# branches ['29->exit', '29->30']

import pytest
from docstring_parser.numpydoc import _clean_str

def test_clean_str_non_empty():
    # Test with a non-empty string
    non_empty_string = "  Some content  "
    result = _clean_str(non_empty_string)
    assert result == "Some content", "The string should be stripped and returned"

def test_clean_str_empty():
    # Test with an empty string
    empty_string = "     "
    result = _clean_str(empty_string)
    assert result is None, "The function should return None for an empty string"
