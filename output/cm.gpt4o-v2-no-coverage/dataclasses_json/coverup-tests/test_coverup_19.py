# file: dataclasses_json/core.py:96-115
# asked: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [99, 112], [103, 104], [103, 105], [112, 113], [112, 114]]}
# gained: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [99, 112], [103, 104], [103, 105], [112, 113], [112, 114]]}

import pytest
from unittest.mock import Mock
from dataclasses_json.core import _encode_overrides, _encode_json_type

def test_encode_overrides_no_overrides():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {}
    result = _encode_overrides(kvs, overrides)
    assert result == kvs

def test_encode_overrides_with_exclude():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    exclude_mock = Mock(return_value=True)
    overrides = {'key1': Mock(exclude=exclude_mock)}
    result = _encode_overrides(kvs, overrides)
    assert result == {'key2': 'value2'}
    exclude_mock.assert_called_once_with('value1')

def test_encode_overrides_with_letter_case():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    letter_case_mock = Mock(side_effect=lambda x: x.upper())
    overrides = {'key1': Mock(letter_case=letter_case_mock, exclude=None, encoder=None)}
    result = _encode_overrides(kvs, overrides)
    assert result == {'KEY1': 'value1', 'key2': 'value2'}
    letter_case_mock.assert_called_once_with('key1')

def test_encode_overrides_with_encoder():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    encoder_mock = Mock(side_effect=lambda x: f"encoded_{x}")
    overrides = {'key1': Mock(encoder=encoder_mock, exclude=None, letter_case=None)}
    result = _encode_overrides(kvs, overrides)
    assert result == {'key1': 'encoded_value1', 'key2': 'value2'}
    encoder_mock.assert_called_once_with('value1')

def test_encode_overrides_with_encode_json(monkeypatch):
    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {}
    encode_json_type_mock = Mock(side_effect=lambda x: f"json_{x}")
    monkeypatch.setattr('dataclasses_json.core._encode_json_type', encode_json_type_mock)
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert result == {'key1': 'json_value1', 'key2': 'json_value2'}
    encode_json_type_mock.assert_any_call('value1')
    encode_json_type_mock.assert_any_call('value2')

def test_encode_overrides_full():
    kvs = {'key1': 'value1', 'key2': 'value2'}
    exclude_mock = Mock(return_value=False)
    letter_case_mock = Mock(side_effect=lambda x: x.upper())
    encoder_mock = Mock(side_effect=lambda x: f"encoded_{x}")
    overrides = {'key1': Mock(exclude=exclude_mock, letter_case=letter_case_mock, encoder=encoder_mock)}
    result = _encode_overrides(kvs, overrides)
    assert result == {'KEY1': 'encoded_value1', 'key2': 'value2'}
    exclude_mock.assert_called_once_with('value1')
    letter_case_mock.assert_called_once_with('key1')
    encoder_mock.assert_called_once_with('value1')
