# file: string_utils/validation.py:345-365
# asked: {"lines": [345, 359, 360, 361, 362, 363, 365], "branches": [[359, 360], [359, 365]]}
# gained: {"lines": [345, 359, 360, 361, 362, 363, 365], "branches": [[359, 360], [359, 365]]}

import pytest
import json
from string_utils.validation import is_json
from string_utils._regex import JSON_WRAPPER_RE

def test_is_json_valid_dict():
    assert is_json('{"name": "Peter"}') == True

def test_is_json_valid_list():
    assert is_json('[1, 2, 3]') == True

def test_is_json_invalid_json():
    assert is_json('{nope}') == False

def test_is_json_empty_string():
    assert is_json('') == False

def test_is_json_none():
    assert is_json(None) == False

def test_is_json_non_json_string():
    assert is_json('hello') == False

def test_is_json_invalid_type():
    assert is_json(123) == False

def test_is_json_invalid_json_structure():
    assert is_json('{"name": "Peter"') == False

def test_is_json_overflow_error(monkeypatch):
    def mock_loads(s):
        raise OverflowError
    monkeypatch.setattr('json.loads', mock_loads)
    assert is_json('{"name": "Peter"}') == False

def test_is_json_type_error(monkeypatch):
    def mock_loads(s):
        raise TypeError
    monkeypatch.setattr('json.loads', mock_loads)
    assert is_json('{"name": "Peter"}') == False

def test_is_json_value_error(monkeypatch):
    def mock_loads(s):
        raise ValueError
    monkeypatch.setattr('json.loads', mock_loads)
    assert is_json('{"name": "Peter"}') == False
