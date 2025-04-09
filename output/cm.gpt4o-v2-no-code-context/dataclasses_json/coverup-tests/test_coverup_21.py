# file: dataclasses_json/core.py:96-115
# asked: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [99, 112], [103, 104], [103, 105], [112, 113], [112, 114]]}
# gained: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [103, 104], [103, 105], [112, 113], [112, 114]]}

import pytest
from unittest.mock import Mock

# Assuming _encode_json_type is defined somewhere in the module
from dataclasses_json.core import _encode_json_type, _encode_overrides

def test_encode_overrides_with_exclude(monkeypatch):
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {
        'key1': Mock(exclude=lambda x: x == 'value1', letter_case=None, encoder=None),
        'key2': Mock(exclude=lambda x: False, letter_case=None, encoder=None)
    }
    
    result = _encode_overrides(kvs, overrides)
    assert result == {'key2': 'value2'}

def test_encode_overrides_with_letter_case(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=None, letter_case=str.upper, encoder=None)
    }
    
    result = _encode_overrides(kvs, overrides)
    assert result == {'KEY1': 'value1'}

def test_encode_overrides_with_encoder(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=None, letter_case=None, encoder=lambda x: x.upper())
    }
    
    result = _encode_overrides(kvs, overrides)
    assert result == {'key1': 'VALUE1'}

def test_encode_overrides_with_encode_json(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=None, letter_case=None, encoder=None)
    }
    
    mock_encode_json_type = Mock(return_value='encoded_value1')
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)
    
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert result == {'key1': 'encoded_value1'}
    mock_encode_json_type.assert_called_once_with('value1')

def test_encode_overrides_with_all_features(monkeypatch):
    kvs = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=str.upper, encoder=lambda x: x.upper()),
        'key2': Mock(exclude=lambda x: True, letter_case=None, encoder=None),
        'key3': Mock(exclude=None, letter_case=None, encoder=None)
    }
    
    mock_encode_json_type = Mock(side_effect=lambda x: f'encoded_{x}')
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)
    
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert result == {'KEY1': 'encoded_VALUE1', 'key3': 'encoded_value3'}
    mock_encode_json_type.assert_any_call('VALUE1')
    mock_encode_json_type.assert_any_call('value3')
