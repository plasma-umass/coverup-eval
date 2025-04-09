# file: string_utils/manipulation.py:405-430
# asked: {"lines": [405, 429, 430], "branches": []}
# gained: {"lines": [405, 429, 430], "branches": []}

import pytest
from string_utils.manipulation import prettify
from string_utils.errors import InvalidInputError

def test_prettify_basic():
    input_string = ' unprettified string ,, like this one,will be"prettified" .it\' s awesome! '
    expected_output = 'Unprettified string, like this one, will be "prettified". It\'s awesome!'
    assert prettify(input_string) == expected_output

def test_prettify_no_spaces():
    input_string = 'NoSpacesHere'
    expected_output = 'Nospaceshere'
    assert prettify(input_string.lower()) == expected_output

def test_prettify_multiple_spaces():
    input_string = 'Multiple   spaces   here'
    expected_output = 'Multiple spaces here'
    assert prettify(input_string) == expected_output

def test_prettify_arithmetic_operators():
    input_string = '1+1=2'
    expected_output = '1 + 1 = 2'
    assert prettify(input_string) == expected_output

def test_prettify_punctuation():
    input_string = 'Hello,world!How are you?'
    expected_output = 'Hello, world! How are you?'
    assert prettify(input_string) == expected_output

def test_prettify_quotes():
    input_string = 'He said"hello"to her'
    expected_output = 'He said "hello" to her'
    assert prettify(input_string) == expected_output

def test_prettify_brackets():
    input_string = 'This is(foo)bar'
    expected_output = 'This is (foo) bar'
    assert prettify(input_string) == expected_output

def test_prettify_percentage():
    input_string = '100 % sure'
    expected_output = '100% sure'
    assert prettify(input_string) == expected_output

def test_prettify_saxon_genitive():
    input_string = "Dave' s dog"
    expected_output = "Dave's dog"
    assert prettify(input_string) == expected_output

def test_prettify_invalid_input(mocker):
    mocker.patch('string_utils.validation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        prettify(123)
