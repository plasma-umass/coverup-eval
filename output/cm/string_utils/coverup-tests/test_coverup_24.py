# file string_utils/manipulation.py:529-558
# lines [529, 551, 552, 554, 555, 556, 558]
# branches ['551->552', '551->554']

import pytest
from string_utils.manipulation import strip_margin

# Assuming the InvalidInputError is defined in string_utils.errors
from string_utils.errors import InvalidInputError

def test_strip_margin():
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

def test_strip_margin_with_invalid_input():
    with pytest.raises(InvalidInputError):
        strip_margin(123)  # Non-string input should raise InvalidInputError
