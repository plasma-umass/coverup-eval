# file: dataclasses_json/core.py:96-115
# asked: {"lines": [], "branches": [[99, 112]]}
# gained: {"lines": [], "branches": [[99, 112]]}

import pytest
from unittest.mock import Mock

# Assuming _encode_overrides is imported from dataclasses_json.core
from dataclasses_json.core import _encode_overrides

def test_encode_overrides_with_exclude(monkeypatch):
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {
        'key1': Mock(exclude=lambda x: True, letter_case=None, encoder=None),
        'key2': Mock(exclude=lambda x: False, letter_case=None, encoder=None)
    }
    
    result = _encode_overrides(kvs, overrides)
    assert 'key1' not in result
    assert 'key2' in result
    assert result['key2'] == 'value2'

def test_encode_overrides_with_letter_case(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=str.upper, encoder=None)
    }
    
    result = _encode_overrides(kvs, overrides)
    assert 'KEY1' in result
    assert result['KEY1'] == 'value1'

def test_encode_overrides_with_encoder(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=None, encoder=lambda x: x.upper())
    }
    
    result = _encode_overrides(kvs, overrides)
    assert 'key1' in result
    assert result['key1'] == 'VALUE1'

def test_encode_overrides_with_encode_json(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {
        'key1': Mock(exclude=lambda x: False, letter_case=None, encoder=None)
    }
    
    def mock_encode_json_type(value):
        return f"encoded_{value}"
    
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)
    
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert 'key1' in result
    assert result['key1'] == 'encoded_value1'

def test_encode_overrides_with_exclude_and_encode_json(monkeypatch):
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {
        'key1': Mock(exclude=lambda x: True, letter_case=None, encoder=None),
        'key2': Mock(exclude=lambda x: False, letter_case=None, encoder=None)
    }
    
    def mock_encode_json_type(value):
        return f"encoded_{value}"
    
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)
    
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert 'key1' not in result
    assert 'key2' in result
    assert result['key2'] == 'encoded_value2'

def test_encode_overrides_with_no_overrides_and_encode_json(monkeypatch):
    kvs = {'key1': 'value1'}
    overrides = {}
    
    def mock_encode_json_type(value):
        return f"encoded_{value}"
    
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)
    
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert 'key1' in result
    assert result['key1'] == 'encoded_value1'
