# file: string_utils/manipulation.py:241-242
# asked: {"lines": [241, 242], "branches": []}
# gained: {"lines": [241, 242], "branches": []}

import pytest
import re
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    # Provide a dummy input string to satisfy the constructor
    return __StringFormatter("dummy")

def test_fix_saxon_genitive(string_formatter):
    # Create a mock regex match object
    class MockRegexMatch:
        def group(self, index):
            return "John 's"

    mock_match = MockRegexMatch()
    result = string_formatter._StringFormatter__fix_saxon_genitive(mock_match)
    
    assert result == "John's "
