# file: string_utils/validation.py:345-365
# asked: {"lines": [345, 359, 360, 361, 362, 363, 365], "branches": [[359, 360], [359, 365]]}
# gained: {"lines": [345, 359, 360, 361, 362, 363, 365], "branches": [[359, 360], [359, 365]]}

import pytest
from string_utils.validation import is_json

def test_is_json_valid_dict():
    assert is_json('{"name": "Peter"}') == True

def test_is_json_valid_list():
    assert is_json('[1, 2, 3]') == True

def test_is_json_invalid():
    assert is_json('{nope}') == False

def test_is_json_empty_string():
    assert is_json('') == False

def test_is_json_none():
    assert is_json(None) == False

def test_is_json_non_json_string():
    assert is_json('hello') == False

def test_is_json_invalid_json_structure():
    assert is_json('{"name": "Peter",}') == False
