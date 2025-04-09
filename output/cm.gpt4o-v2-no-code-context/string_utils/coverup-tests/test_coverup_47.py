# file: string_utils/manipulation.py:235-236
# asked: {"lines": [235, 236], "branches": []}
# gained: {"lines": [235, 236], "branches": []}

import pytest
import re
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    # Provide a dummy input string to satisfy the constructor
    return __StringFormatter("dummy")

def test_ensure_spaces_around(string_formatter):
    # Create a mock regex match object
    class MockMatch:
        def group(self, index):
            return "  test  "
    
    mock_match = MockMatch()
    
    # Call the private method using the class instance
    result = string_formatter._StringFormatter__ensure_spaces_around(mock_match)
    
    # Assert the expected result
    assert result == " test "
