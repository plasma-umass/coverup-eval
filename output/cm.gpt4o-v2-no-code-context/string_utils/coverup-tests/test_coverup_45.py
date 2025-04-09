# file: string_utils/manipulation.py:222-223
# asked: {"lines": [222, 223], "branches": []}
# gained: {"lines": [222, 223], "branches": []}

import pytest
import re
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    return __StringFormatter("dummy_string")

def test_remove_duplicates(string_formatter):
    # Create a mock regex match object
    class MockMatch:
        def group(self, index):
            return "aaabbbccc"
    
    mock_match = MockMatch()
    
    # Call the private method using the class instance
    result = string_formatter._StringFormatter__remove_duplicates(mock_match)
    
    # Assert the expected result
    assert result == "a"
