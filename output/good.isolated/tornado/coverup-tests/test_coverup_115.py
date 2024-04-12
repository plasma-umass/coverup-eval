# file tornado/escape.py:178-180
# lines [178, 179, 180]
# branches []

import pytest
from tornado.escape import utf8

def test_utf8_with_string():
    # Test the utf8 function with a string input
    input_str = "Hello, world!"
    expected_output = b"Hello, world!"
    
    # Call the utf8 function and assert the output is as expected
    output = utf8(input_str)
    assert output == expected_output
