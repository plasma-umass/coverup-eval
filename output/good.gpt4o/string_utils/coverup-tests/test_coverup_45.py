# file string_utils/manipulation.py:222-223
# lines [222, 223]
# branches []

import pytest
import re
from string_utils.manipulation import __StringFormatter

def test___remove_duplicates():
    # Create a mock regex match object
    class MockMatch:
        def __init__(self, group):
            self._group = group
        
        def group(self, index):
            return self._group
    
    # Create a dummy input string to satisfy the constructor
    dummy_input_string = ""
    formatter = __StringFormatter(dummy_input_string)
    
    # Test case where the group has duplicates
    mock_match = MockMatch("aaabbbccc")
    result = formatter._StringFormatter__remove_duplicates(mock_match)
    assert result == 'a', "Expected 'a' but got {}".format(result)
    
    # Test case where the group has no duplicates
    mock_match = MockMatch("abc")
    result = formatter._StringFormatter__remove_duplicates(mock_match)
    assert result == 'a', "Expected 'a' but got {}".format(result)
    
    # Test case where the group is a single character
    mock_match = MockMatch("a")
    result = formatter._StringFormatter__remove_duplicates(mock_match)
    assert result == 'a', "Expected 'a' but got {}".format(result)
