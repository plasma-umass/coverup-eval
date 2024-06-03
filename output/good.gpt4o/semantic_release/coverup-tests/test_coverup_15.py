# file semantic_release/helpers.py:9-13
# lines [9, 10, 11, 13]
# branches ['10->11', '10->13']

import pytest
from semantic_release.helpers import format_arg

def test_format_arg():
    # Test with a string value
    assert format_arg("  test  ") == "'test'"
    
    # Test with a non-string value
    assert format_arg(123) == "123"
    
    # Test with an empty string
    assert format_arg("  ") == "''"
    
    # Test with a string containing only whitespace
    assert format_arg("   ") == "''"
    
    # Test with a string containing special characters
    assert format_arg("  !@#  ") == "'!@#'"
    
    # Test with a None value
    assert format_arg(None) == "None"
    
    # Test with a boolean value
    assert format_arg(True) == "True"
    assert format_arg(False) == "False"
