# file: dataclasses_json/core.py:96-115
# asked: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [99, 112], [103, 104], [103, 105], [112, 113], [112, 114]]}
# gained: {"lines": [96, 97, 98, 99, 100, 103, 104, 105, 106, 107, 109, 110, 112, 113, 114, 115], "branches": [[98, 99], [98, 115], [99, 100], [99, 112], [103, 104], [103, 105], [112, 113], [112, 114]]}

import pytest

class MockOverride:
    def __init__(self, exclude=None, letter_case=None, encoder=None):
        self.exclude = exclude
        self.letter_case = letter_case
        self.encoder = encoder

def test_encode_overrides_no_overrides():
    from dataclasses_json.core import _encode_overrides

    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {}
    result = _encode_overrides(kvs, overrides)
    assert result == kvs

def test_encode_overrides_with_exclude():
    from dataclasses_json.core import _encode_overrides

    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {'key1': MockOverride(exclude=lambda x: x == 'value1')}
    result = _encode_overrides(kvs, overrides)
    assert result == {'key2': 'value2'}

def test_encode_overrides_with_letter_case():
    from dataclasses_json.core import _encode_overrides

    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {'key1': MockOverride(letter_case=str.upper)}
    result = _encode_overrides(kvs, overrides)
    assert result == {'KEY1': 'value1', 'key2': 'value2'}

def test_encode_overrides_with_encoder():
    from dataclasses_json.core import _encode_overrides

    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {'key1': MockOverride(encoder=lambda x: x.upper())}
    result = _encode_overrides(kvs, overrides)
    assert result == {'key1': 'VALUE1', 'key2': 'value2'}

def test_encode_overrides_with_encode_json(monkeypatch):
    from dataclasses_json.core import _encode_overrides, _encode_json_type

    kvs = {'key1': 'value1', 'key2': 'value2'}
    overrides = {}

    def mock_encode_json_type(value):
        return f"encoded_{value}"

    monkeypatch.setattr('dataclasses_json.core._encode_json_type', mock_encode_json_type)
    result = _encode_overrides(kvs, overrides, encode_json=True)
    assert result == {'key1': 'encoded_value1', 'key2': 'encoded_value2'}
