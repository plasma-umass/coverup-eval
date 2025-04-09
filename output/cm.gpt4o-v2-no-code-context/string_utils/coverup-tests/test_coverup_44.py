# file: string_utils/manipulation.py:219-220
# asked: {"lines": [219, 220], "branches": []}
# gained: {"lines": [219, 220], "branches": []}

import pytest
import re
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    # Provide a dummy input string to satisfy the constructor
    return __StringFormatter("dummy")

def test_uppercase_first_char(string_formatter):
    # Create a mock regex match object
    class MockMatch:
        def group(self, index):
            return "test"

    mock_match = MockMatch()
    
    # Call the private method using the class instance
    result = string_formatter._StringFormatter__uppercase_first_char(mock_match)
    
    # Assert the result is as expected
    assert result == "TEST"
