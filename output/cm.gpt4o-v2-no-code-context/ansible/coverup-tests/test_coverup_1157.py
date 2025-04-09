# file: lib/ansible/module_utils/common/json.py:26-39
# asked: {"lines": [32, 33, 34, 35, 36, 37, 39], "branches": [[32, 33], [32, 34], [34, 35], [34, 36], [36, 37], [36, 39]]}
# gained: {"lines": [32, 33, 34, 35, 36, 37, 39], "branches": [[32, 33], [32, 34], [34, 35], [34, 36], [36, 37], [36, 39]]}

import pytest
from unittest.mock import patch
from ansible.module_utils.common.json import _preprocess_unsafe_encode

# Mock functions to simulate the behavior of _is_unsafe, to_text, is_sequence, and Mapping
def test_preprocess_unsafe_encode_with_unsafe_value(monkeypatch):
    def mock_is_unsafe(value):
        return True

    def mock_to_text(value, errors, nonstring):
        return str(value)

    monkeypatch.setattr('ansible.module_utils.common.json._is_unsafe', mock_is_unsafe)
    monkeypatch.setattr('ansible.module_utils.common.json.to_text', mock_to_text)

    value = "unsafe_value"
    result = _preprocess_unsafe_encode(value)
    assert result == {'__ansible_unsafe': 'unsafe_value'}

def test_preprocess_unsafe_encode_with_sequence(monkeypatch):
    def mock_is_unsafe(value):
        return False

    def mock_is_sequence(value):
        return isinstance(value, list)

    monkeypatch.setattr('ansible.module_utils.common.json._is_unsafe', mock_is_unsafe)
    monkeypatch.setattr('ansible.module_utils.common.json.is_sequence', mock_is_sequence)

    value = ["safe_value", "another_safe_value"]
    result = _preprocess_unsafe_encode(value)
    assert result == ["safe_value", "another_safe_value"]

def test_preprocess_unsafe_encode_with_mapping(monkeypatch):
    def mock_is_unsafe(value):
        return False

    def mock_is_sequence(value):
        return False

    class MockMapping(dict):
        pass

    monkeypatch.setattr('ansible.module_utils.common.json._is_unsafe', mock_is_unsafe)
    monkeypatch.setattr('ansible.module_utils.common.json.is_sequence', mock_is_sequence)
    monkeypatch.setattr('ansible.module_utils.common.json.Mapping', MockMapping)

    value = MockMapping(key1="value1", key2="value2")
    result = _preprocess_unsafe_encode(value)
    assert result == {"key1": "value1", "key2": "value2"}
