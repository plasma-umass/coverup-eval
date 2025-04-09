# file string_utils/manipulation.py:529-558
# lines [529, 551, 552, 554, 555, 556, 558]
# branches ['551->552', '551->554']

import pytest
from string_utils.manipulation import strip_margin, InvalidInputError
import re

# Mocking the is_string function and MARGIN_RE pattern
def is_string(input_string):
    return isinstance(input_string, str)

MARGIN_RE = re.compile(r'^\s+')

def test_strip_margin_valid_input():
    input_string = '''
                line 1
                line 2
                line 3
                '''
    expected_output = '''
line 1
line 2
line 3
'''
    assert strip_margin(input_string) == expected_output

def test_strip_margin_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_margin(12345)

def test_strip_margin_empty_string():
    input_string = ''
    expected_output = ''
    assert strip_margin(input_string) == expected_output
