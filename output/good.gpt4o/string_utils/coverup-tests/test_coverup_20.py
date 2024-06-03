# file string_utils/manipulation.py:433-459
# lines [433, 447, 448, 451, 454, 457, 459]
# branches ['447->448', '447->451']

import pytest
from string_utils.manipulation import asciify, InvalidInputError
import unicodedata

def is_string(input_string):
    return isinstance(input_string, str)

def test_asciify_valid_string():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    expected_output = 'eeuuooaaeynAAACIINOE'
    assert asciify(input_string) == expected_output

def test_asciify_invalid_input():
    with pytest.raises(InvalidInputError):
        asciify(12345)  # Non-string input should raise InvalidInputError

def test_asciify_empty_string():
    input_string = ''
    expected_output = ''
    assert asciify(input_string) == expected_output

def test_asciify_ascii_string():
    input_string = 'hello'
    expected_output = 'hello'
    assert asciify(input_string) == expected_output

def test_asciify_mixed_string():
    input_string = 'hello èéùúòóäåëýñÅÀÁÇÌÍÑÓË world'
    expected_output = 'hello eeuuooaaeynAAACIINOE world'
    assert asciify(input_string) == expected_output
