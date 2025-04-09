# file: tornado/options.py:145-146
# asked: {"lines": [145, 146], "branches": []}
# gained: {"lines": [145, 146], "branches": []}

import pytest
from tornado.options import OptionParser

def test_normalize_name():
    parser = OptionParser()
    
    # Test case 1: name with underscores
    assert parser._normalize_name("test_name") == "test-name"
    
    # Test case 2: name without underscores
    assert parser._normalize_name("testname") == "testname"
    
    # Test case 3: name with multiple underscores
    assert parser._normalize_name("test_name_with_underscores") == "test-name-with-underscores"
    
    # Test case 4: empty string
    assert parser._normalize_name("") == ""
    
    # Test case 5: name with leading and trailing underscores
    assert parser._normalize_name("_test_name_") == "-test-name-"
