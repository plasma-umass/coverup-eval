# file tornado/escape.py:86-88
# lines [86, 88]
# branches []

import pytest
from tornado.escape import squeeze

def test_squeeze():
    # Test with a string containing various whitespace characters
    input_str = "Hello\t \nWorld!  This is a\n\ttest."
    expected_str = "Hello World! This is a test."
    assert squeeze(input_str) == expected_str

    # Test with a string that has leading and trailing whitespace
    input_str = "\n\t Hello World! \t\n"
    expected_str = "Hello World!"
    assert squeeze(input_str) == expected_str

    # Test with a string that has no whitespace
    input_str = "HelloWorld!"
    expected_str = "HelloWorld!"
    assert squeeze(input_str) == expected_str

    # Test with an empty string
    input_str = ""
    expected_str = ""
    assert squeeze(input_str) == expected_str

    # Test with a string that is all whitespace
    input_str = "\t\n  \x00\x20"
    expected_str = ""
    assert squeeze(input_str) == expected_str
