# file string_utils/manipulation.py:241-242
# lines [241, 242]
# branches []

import pytest
import re
from string_utils.manipulation import __StringFormatter

def test___fix_saxon_genitive():
    class TestStringFormatter(__StringFormatter):
        def __init__(self):
            pass

    formatter = TestStringFormatter()
    test_string = "John 's book"
    regex = re.compile(r"(John 's)")
    match = regex.search(test_string)
    
    result = formatter._StringFormatter__fix_saxon_genitive(match)
    
    assert result == "John's "
