# file: dataclasses_json/core.py:96-115
# asked: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [99, 112], [103, 104], [103, 105], [112, 113], [112, 114]]}
# gained: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [99, 112], [103, 104], [103, 105], [112, 113], [112, 114]]}

import pytest
from unittest.mock import Mock

# Assuming _encode_json_type is defined somewhere in the module
from dataclasses_json.core import _encode_json_type, _encode_overrides

def test_encode_overrides_no_overrides():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {}
    result = _encode_overrides(kvs, overrides)
    assert result == kvs

def test_encode_overrides_with_exclude():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {
        'key1': Mock(exclude=lambda x: True, letter_case=None, encoder=None),
        'key2': Mock(exclude=lambda x: False, letter_case=None, encoder=None)
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {'key2': 'value2'}

def test_encode_overrides_with_letter_case():
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=str.upper, encoder=None)
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {'KEY1': 'value1'}

def test_encode_overrides_with_encoder():
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=None, encoder=str.upper)
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {'key1': 'VALUE1'}

def test_encode_overrides_with_encode_json(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {}
    
    def mock_encode_json_type(value):
        return f"encoded_{value}"
    
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)
    
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert result == {'key1': 'encoded_value1'}

def test_encode_overrides_full():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=str.upper, encoder=str.lower),
        'key2': Mock(exclude=lambda x: False, letter_case=None, encoder=str.upper)
    }
    result = _encode_overrides(kvs, overrides)
    assert result == {'KEY1': 'value1', 'key2': 'VALUE2'}
