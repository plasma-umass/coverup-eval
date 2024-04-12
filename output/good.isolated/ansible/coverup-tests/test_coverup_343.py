# file lib/ansible/module_utils/common/json.py:26-39
# lines [26, 32, 33, 34, 35, 36, 37, 39]
# branches ['32->33', '32->34', '34->35', '34->36', '36->37', '36->39']

import pytest
from ansible.module_utils.common.json import _preprocess_unsafe_encode
from ansible.module_utils._text import to_text
from collections.abc import Mapping

# Mocking the AnsibleUnsafeText since the import failed
class AnsibleUnsafeText(str):
    pass

def is_sequence(value):
    return isinstance(value, (list, tuple))

def _is_unsafe(value):
    return isinstance(value, AnsibleUnsafeText)

@pytest.fixture
def mock_is_sequence(mocker):
    return mocker.patch('ansible.module_utils.common.json.is_sequence', side_effect=is_sequence)

@pytest.fixture
def mock_is_unsafe(mocker):
    return mocker.patch('ansible.module_utils.common.json._is_unsafe', side_effect=_is_unsafe)

def test_preprocess_unsafe_encode_with_unsafe(mock_is_unsafe, mock_is_sequence):
    unsafe_value = AnsibleUnsafeText('unsafe_text')
    result = _preprocess_unsafe_encode(unsafe_value)
    assert result == {'__ansible_unsafe': to_text(unsafe_value, errors='surrogate_or_strict', nonstring='strict')}

def test_preprocess_unsafe_encode_with_sequence(mock_is_unsafe, mock_is_sequence):
    unsafe_value = AnsibleUnsafeText('unsafe_text')
    sequence = [unsafe_value, 'safe_text']
    result = _preprocess_unsafe_encode(sequence)
    assert result == [{'__ansible_unsafe': to_text(unsafe_value, errors='surrogate_or_strict', nonstring='strict')}, 'safe_text']

def test_preprocess_unsafe_encode_with_mapping(mock_is_unsafe, mock_is_sequence):
    unsafe_value = AnsibleUnsafeText('unsafe_text')
    mapping = {'key1': unsafe_value, 'key2': 'safe_text'}
    result = _preprocess_unsafe_encode(mapping)
    assert result == {
        'key1': {'__ansible_unsafe': to_text(unsafe_value, errors='surrogate_or_strict', nonstring='strict')},
        'key2': 'safe_text'
    }
