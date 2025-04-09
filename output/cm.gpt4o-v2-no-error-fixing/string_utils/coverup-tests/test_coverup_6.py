# file: string_utils/manipulation.py:529-558
# asked: {"lines": [529, 551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}
# gained: {"lines": [529, 551, 552, 554, 555, 556, 558], "branches": [[551, 552], [551, 554]]}

import pytest
from string_utils.manipulation import strip_margin
from string_utils.errors import InvalidInputError

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
    with pytest.raises(InvalidInputError) as excinfo:
        strip_margin(12345)
    assert str(excinfo.value) == 'Expected "str", received "int"'
