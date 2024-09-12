# file: string_utils/manipulation.py:222-223
# asked: {"lines": [222, 223], "branches": []}
# gained: {"lines": [222, 223], "branches": []}

import re
import pytest
from string_utils.manipulation import __StringFormatter

def test_remove_duplicates():
    formatter = __StringFormatter("dummy")
    regex_match = re.match(r"(.)\1*", "aabbcc")
    result = formatter._StringFormatter__remove_duplicates(regex_match)
    assert result == "a"

    regex_match = re.match(r"(.)\1*", "bbccdd")
    result = formatter._StringFormatter__remove_duplicates(regex_match)
    assert result == "b"

    regex_match = re.match(r"(.)\1*", "ccddeeff")
    result = formatter._StringFormatter__remove_duplicates(regex_match)
    assert result == "c"
