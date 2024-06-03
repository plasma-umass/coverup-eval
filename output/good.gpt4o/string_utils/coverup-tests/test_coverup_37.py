# file string_utils/manipulation.py:235-236
# lines [235, 236]
# branches []

import pytest
from string_utils.manipulation import __StringFormatter

def test___ensure_spaces_around():
    class MockMatch:
        def group(self, index):
            return "  test  "
    
    mock_match = MockMatch()
    formatter = __StringFormatter.__new__(__StringFormatter)
    result = formatter._StringFormatter__ensure_spaces_around(mock_match)
    
    assert result == " test "
