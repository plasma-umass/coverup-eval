# file tornado/options.py:145-146
# lines [145, 146]
# branches []

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_normalize_name(option_parser):
    # Test with underscores
    assert option_parser._normalize_name("test_name") == "test-name"
    
    # Test with no underscores
    assert option_parser._normalize_name("testname") == "testname"
    
    # Test with multiple underscores
    assert option_parser._normalize_name("test_name_with_underscores") == "test-name-with-underscores"
    
    # Test with leading and trailing underscores
    assert option_parser._normalize_name("_test_name_") == "-test-name-"
    
    # Test with empty string
    assert option_parser._normalize_name("") == ""
    
    # Test with only underscores
    assert option_parser._normalize_name("___") == "---"
