# file: string_utils/validation.py:345-365
# asked: {"lines": [345, 359, 360, 361, 362, 363, 365], "branches": [[359, 360], [359, 365]]}
# gained: {"lines": [345, 359, 360, 361, 362, 363, 365], "branches": [[359, 360], [359, 365]]}

import pytest
import json
from string_utils.validation import is_json

def test_is_json_valid_dict():
    assert is_json('{"name": "Peter"}') is True

def test_is_json_valid_list():
    assert is_json('[1, 2, 3]') is True

def test_is_json_invalid_string():
    assert is_json('{nope}') is False

def test_is_json_non_string_input():
    assert is_json(12345) is False

def test_is_json_empty_string():
    assert is_json('') is False

def test_is_json_invalid_json_syntax():
    assert is_json('{"name": "Peter"') is False

def test_is_json_invalid_json_type():
    assert is_json('{"name": "Peter"}]') is False

def test_is_json_overflow_error(monkeypatch):
    def mock_loads(s):
        raise OverflowError
    monkeypatch.setattr(json, 'loads', mock_loads)
    assert is_json('{"name": "Peter"}') is False

def test_is_json_type_error(monkeypatch):
    def mock_loads(s):
        raise TypeError
    monkeypatch.setattr(json, 'loads', mock_loads)
    assert is_json('{"name": "Peter"}') is False

def test_is_json_value_error(monkeypatch):
    def mock_loads(s):
        raise ValueError
    monkeypatch.setattr(json, 'loads', mock_loads)
    assert is_json('{"name": "Peter"}') is False
