# file: string_utils/manipulation.py:222-223
# asked: {"lines": [222, 223], "branches": []}
# gained: {"lines": [222, 223], "branches": []}

import pytest
import re
from string_utils.manipulation import __StringFormatter

class MockMatch:
    def __init__(self, group1):
        self.group1 = group1

    def group(self, index):
        if index == 1:
            return self.group1
        return None

@pytest.fixture
def formatter():
    return __StringFormatter("test")

def test_remove_duplicates(formatter):
    match = MockMatch("aabbcc")
    result = formatter._StringFormatter__remove_duplicates(match)
    assert result == "a"

