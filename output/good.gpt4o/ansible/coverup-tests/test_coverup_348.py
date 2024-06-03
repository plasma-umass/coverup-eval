# file lib/ansible/module_utils/common/json.py:26-39
# lines [26, 32, 33, 34, 35, 36, 37, 39]
# branches ['32->33', '32->34', '34->35', '34->36', '36->37', '36->39']

import pytest
from unittest.mock import patch
from ansible.module_utils.common.json import _preprocess_unsafe_encode

class AnsibleUnsafe:
    def __init__(self, value):
        self.value = value

def _is_unsafe(value):
    return isinstance(value, AnsibleUnsafe)

def to_text(value, errors='strict', nonstring='strict'):
    if isinstance(value, AnsibleUnsafe):
        return str(value.value)
    return str(value)

def is_sequence(value):
    return isinstance(value, (list, tuple))

def test_preprocess_unsafe_encode_with_unsafe_value():
    value = AnsibleUnsafe("unsafe_value")
    with patch('ansible.module_utils.common.json._is_unsafe', _is_unsafe), \
         patch('ansible.module_utils.common.json.to_text', to_text):
        result = _preprocess_unsafe_encode(value)
    assert result == {'__ansible_unsafe': 'unsafe_value'}

def test_preprocess_unsafe_encode_with_sequence():
    value = [AnsibleUnsafe("unsafe_value1"), AnsibleUnsafe("unsafe_value2")]
    with patch('ansible.module_utils.common.json._is_unsafe', _is_unsafe), \
         patch('ansible.module_utils.common.json.to_text', to_text):
        result = _preprocess_unsafe_encode(value)
    assert result == [{'__ansible_unsafe': 'unsafe_value1'}, {'__ansible_unsafe': 'unsafe_value2'}]

def test_preprocess_unsafe_encode_with_mapping():
    value = {'key1': AnsibleUnsafe("unsafe_value1"), 'key2': AnsibleUnsafe("unsafe_value2")}
    with patch('ansible.module_utils.common.json._is_unsafe', _is_unsafe), \
         patch('ansible.module_utils.common.json.to_text', to_text):
        result = _preprocess_unsafe_encode(value)
    assert result == {'key1': {'__ansible_unsafe': 'unsafe_value1'}, 'key2': {'__ansible_unsafe': 'unsafe_value2'}}

def test_preprocess_unsafe_encode_with_nested_structure():
    value = {
        'key1': [AnsibleUnsafe("unsafe_value1"), {'nested_key': AnsibleUnsafe("unsafe_value2")}],
        'key2': [AnsibleUnsafe("unsafe_value3")]
    }
    with patch('ansible.module_utils.common.json._is_unsafe', _is_unsafe), \
         patch('ansible.module_utils.common.json.to_text', to_text):
        result = _preprocess_unsafe_encode(value)
    assert result == {
        'key1': [{'__ansible_unsafe': 'unsafe_value1'}, {'nested_key': {'__ansible_unsafe': 'unsafe_value2'}}],
        'key2': [{'__ansible_unsafe': 'unsafe_value3'}]
    }
