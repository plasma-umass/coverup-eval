# file src/blib2to3/pgen2/tokenize.py:66-67
# lines [66, 67]
# branches []

import pytest
from blib2to3.pgen2 import tokenize

def test_any_function():
    # Mock the group function to return a simple string
    tokenize.group = lambda *args: ''.join(args)
    
    # Test the any function with multiple choices
    result = tokenize.any('a', 'b', 'c')
    assert result == 'abc*'

    # Test the any function with a single choice
    result = tokenize.any('x')
    assert result == 'x*'

    # Test the any function with no choices
    result = tokenize.any()
    assert result == '*'

    # Clean up by deleting the mock
    del tokenize.group
