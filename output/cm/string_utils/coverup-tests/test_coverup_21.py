# file string_utils/manipulation.py:222-223
# lines [222, 223]
# branches []

import pytest
import re
from string_utils.manipulation import __StringFormatter

class StringFormatter(__StringFormatter):
    def __init__(self):
        super().__init__('')

@pytest.fixture
def string_formatter():
    return StringFormatter()

def test_remove_duplicates(string_formatter, mocker):
    # Mock the regex match object to return a specific group
    mock_match = mocker.Mock()
    mock_match.group.return_value = 'aa'

    # Call the private method directly since it's not accessible otherwise
    result = string_formatter._StringFormatter__remove_duplicates(mock_match)

    # Assert that the result is as expected
    assert result == 'a'
