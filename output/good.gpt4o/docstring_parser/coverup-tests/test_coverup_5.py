# file docstring_parser/numpydoc.py:27-30
# lines [27, 28, 29, 30]
# branches ['29->exit', '29->30']

import pytest
from docstring_parser.numpydoc import _clean_str

def test_clean_str():
    # Test with a string that has leading and trailing spaces
    assert _clean_str("  test  ") == "test"
    
    # Test with a string that has only spaces
    assert _clean_str("   ") is None
    
    # Test with an empty string
    assert _clean_str("") is None
    
    # Test with a string that has no leading or trailing spaces
    assert _clean_str("test") == "test"
    
    # Test with a string that has leading spaces
    assert _clean_str("  test") == "test"
    
    # Test with a string that has trailing spaces
    assert _clean_str("test  ") == "test"
