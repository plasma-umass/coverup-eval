# file string_utils/manipulation.py:229-230
# lines [230]
# branches []

import pytest
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    return __StringFormatter("dummy input")

def test_ensure_right_space_only(string_formatter):
    # Mocking a regex match with a group method that returns a string with spaces
    class MockMatch:
        def group(self, index):
            return '  text with spaces  '

    mock_match = MockMatch()
    result = string_formatter._StringFormatter__ensure_right_space_only(mock_match)
    assert result == 'text with spaces ', "The function should return the string with right space only"
