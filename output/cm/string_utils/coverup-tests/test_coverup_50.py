# file string_utils/manipulation.py:241-242
# lines [242]
# branches []

import pytest
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    return __StringFormatter("dummy input string")

def test_fix_saxon_genitive(string_formatter):
    # Create a regex match object that matches the pattern expected by __fix_saxon_genitive
    import re
    pattern = re.compile(r"(\w+'s\s)")
    match = pattern.search("John's book")

    # Call the private method __fix_saxon_genitive directly
    result = string_formatter._StringFormatter__fix_saxon_genitive(match)

    # Assert that the result is as expected
    assert result == "John's "

    # No cleanup is necessary as no state is modified outside the scope of the test
