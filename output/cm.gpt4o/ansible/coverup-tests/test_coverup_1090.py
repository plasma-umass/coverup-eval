# file lib/ansible/module_utils/common/json.py:42-82
# lines [54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 71, 72, 80]
# branches ['54->56', '54->60', '56->57', '56->59', '60->62', '60->63', '63->65', '63->66', '66->68', '66->71', '79->80']

import json
import datetime
from collections.abc import Mapping
import pytest
from unittest.mock import MagicMock

# Assuming the AnsibleJSONEncoder class is defined in ansible.module_utils.common.json
from ansible.module_utils.common.json import AnsibleJSONEncoder

class EncryptedObject:
    __ENCRYPTED__ = True
    _ciphertext = "encrypted_data"

class UnsafeObject:
    __UNSAFE__ = True

class CustomMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

def test_ansible_json_encoder_encrypted_object(mocker):
    obj = EncryptedObject()
    mock_to_text = mocker.patch('ansible.module_utils.common.json.to_text', return_value="encrypted_data")
    
    encoder = AnsibleJSONEncoder(vault_to_text=True)
    result = encoder.default(obj)
    assert result == "encrypted_data"
    mock_to_text.assert_called_once_with(obj, errors='surrogate_or_strict')

    mock_to_text.reset_mock()
    encoder = AnsibleJSONEncoder(vault_to_text=False)
    result = encoder.default(obj)
    assert result == {'__ansible_vault': 'encrypted_data'}
    mock_to_text.assert_called_once_with(obj._ciphertext, errors='surrogate_or_strict', nonstring='strict')

def test_ansible_json_encoder_unsafe_object(mocker):
    obj = UnsafeObject()
    mock_to_text = mocker.patch('ansible.module_utils.common.json.to_text', return_value="unsafe_data")
    
    encoder = AnsibleJSONEncoder()
    result = encoder.default(obj)
    assert result == {'__ansible_unsafe': 'unsafe_data'}
    mock_to_text.assert_called_once_with(obj, errors='surrogate_or_strict', nonstring='strict')

def test_ansible_json_encoder_mapping():
    obj = CustomMapping({'key': 'value'})
    encoder = AnsibleJSONEncoder()
    result = encoder.default(obj)
    assert result == {'key': 'value'}

def test_ansible_json_encoder_date():
    obj = datetime.date(2023, 1, 1)
    encoder = AnsibleJSONEncoder()
    result = encoder.default(obj)
    assert result == '2023-01-01'

    obj = datetime.datetime(2023, 1, 1, 12, 0, 0)
    result = encoder.default(obj)
    assert result == '2023-01-01T12:00:00'

def test_ansible_json_encoder_default(mocker):
    obj = set([1, 2, 3])
    mock_super_default = mocker.patch('json.JSONEncoder.default', return_value=list(obj))
    
    encoder = AnsibleJSONEncoder()
    result = encoder.default(obj)
    assert result == [1, 2, 3]
    mock_super_default.assert_called_once_with(obj)

def test_ansible_json_encoder_iterencode(mocker):
    mock_preprocess = mocker.patch('ansible.module_utils.common.json._preprocess_unsafe_encode', return_value='processed')
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    result = list(encoder.iterencode('unsafe_string'))
    assert result == list(json.JSONEncoder().iterencode('processed'))
    mock_preprocess.assert_called_once_with('unsafe_string')
