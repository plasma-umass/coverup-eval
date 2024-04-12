# file string_utils/manipulation.py:212-212
# lines [212]
# branches []

import pytest
from string_utils.manipulation import __StringFormatter

def test_string_formatter():
    formatter = __StringFormatter("test string")
    assert formatter is not None
