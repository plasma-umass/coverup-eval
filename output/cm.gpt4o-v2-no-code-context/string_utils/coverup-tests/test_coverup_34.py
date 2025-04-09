# file: string_utils/manipulation.py:433-459
# asked: {"lines": [433, 447, 448, 451, 454, 457, 459], "branches": [[447, 448], [447, 451]]}
# gained: {"lines": [433, 447, 448, 451, 454, 457, 459], "branches": [[447, 448], [447, 451]]}

import pytest
from string_utils.manipulation import asciify, InvalidInputError
import unicodedata

def test_asciify_valid_string():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    expected_output = 'eeuuooaaeynAAACIINOE'
    assert asciify(input_string) == expected_output

def test_asciify_empty_string():
    input_string = ''
    expected_output = ''
    assert asciify(input_string) == expected_output

def test_asciify_non_string_input():
    with pytest.raises(InvalidInputError):
        asciify(12345)

def test_asciify_mixed_string():
    input_string = 'Hello, World! èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    expected_output = 'Hello, World! eeuuooaaeynAAACIINOE'
    assert asciify(input_string) == expected_output

def test_asciify_special_characters():
    input_string = '©®™✓'
    expected_output = 'TM'
    assert asciify(input_string) == expected_output
