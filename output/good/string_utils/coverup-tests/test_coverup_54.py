# file string_utils/manipulation.py:225-227
# lines [226, 227]
# branches []

import pytest
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    return __StringFormatter("dummy")

def test_uppercase_first_letter_after_sign(string_formatter):
    # Create a mock regex match object with a group method that returns a string
    class MockMatch:
        def group(self, index):
            return {1: 'a@b'}[index]

    mock_match = MockMatch()

    # Call the method that needs to be tested
    result = string_formatter._StringFormatter__uppercase_first_letter_after_sign(mock_match)

    # Assert that the result is as expected
    assert result == 'a@B', "The first letter after the sign should be uppercase"
