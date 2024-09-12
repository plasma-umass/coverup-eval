# file: string_utils/manipulation.py:433-459
# asked: {"lines": [447, 448, 451, 454, 457, 459], "branches": [[447, 448], [447, 451]]}
# gained: {"lines": [447, 448, 451, 454, 457, 459], "branches": [[447, 448], [447, 451]]}

import pytest
import unicodedata
from string_utils.manipulation import asciify, InvalidInputError

def is_string(input_string):
    return isinstance(input_string, str)

def test_asciify_valid_string():
    input_string = 'èéùúòóäåëýñÅÀÁÇÌÍÑÓË'
    expected_output = 'eeuuooaaeynAAACIINOE'
    assert asciify(input_string) == expected_output

def test_asciify_empty_string():
    input_string = ''
    expected_output = ''
    assert asciify(input_string) == expected_output

def test_asciify_ascii_string():
    input_string = 'hello world'
    expected_output = 'hello world'
    assert asciify(input_string) == expected_output

def test_asciify_mixed_string():
    input_string = 'hello èéùúòóäåëýñÅÀÁÇÌÍÑÓË world'
    expected_output = 'hello eeuuooaaeynAAACIINOE world'
    assert asciify(input_string) == expected_output

def test_asciify_invalid_input():
    with pytest.raises(InvalidInputError):
        asciify(12345)

def test_asciify_non_string_input(monkeypatch):
    monkeypatch.setattr('string_utils.manipulation.is_string', lambda x: False)
    with pytest.raises(InvalidInputError):
        asciify('èéùúòóäåëýñÅÀÁÇÌÍÑÓË')

def test_asciify_unrepresentable_chars():
    input_string = 'hello 😊'
    expected_output = 'hello '
    assert asciify(input_string) == expected_output
