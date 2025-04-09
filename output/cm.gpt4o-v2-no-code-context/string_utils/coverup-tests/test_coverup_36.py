# file: string_utils/manipulation.py:232-233
# asked: {"lines": [232, 233], "branches": []}
# gained: {"lines": [232, 233], "branches": []}

import pytest
import re
from string_utils.manipulation import __StringFormatter

@pytest.fixture
def string_formatter():
    return __StringFormatter("dummy")

def test_ensure_left_space_only(string_formatter):
    regex_match = re.match(r'(.*)', '  test string  ')
    result = string_formatter._StringFormatter__ensure_left_space_only(regex_match)
    assert result == ' test string'
