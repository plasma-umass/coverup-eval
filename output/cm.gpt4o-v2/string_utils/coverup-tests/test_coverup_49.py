# file: string_utils/manipulation.py:235-236
# asked: {"lines": [235, 236], "branches": []}
# gained: {"lines": [235, 236], "branches": []}

import pytest
import re
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def formatter():
    return __StringFormatter("dummy string")

def test_ensure_spaces_around(formatter):
    class MockMatch:
        def group(self, index):
            return "  test  "
    
    mock_match = MockMatch()
    result = formatter._StringFormatter__ensure_spaces_around(mock_match)
    assert result == " test "
