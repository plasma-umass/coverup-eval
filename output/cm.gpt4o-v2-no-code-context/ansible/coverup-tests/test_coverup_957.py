# file: lib/ansible/module_utils/common/json.py:42-82
# asked: {"lines": [54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 71, 72, 80], "branches": [[54, 56], [54, 60], [56, 57], [56, 59], [60, 62], [60, 63], [63, 65], [63, 66], [66, 68], [66, 71], [79, 80]]}
# gained: {"lines": [54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 71, 72, 80], "branches": [[54, 56], [54, 60], [56, 57], [56, 59], [60, 62], [60, 63], [63, 65], [63, 66], [66, 68], [66, 71], [79, 80]]}

import json
import datetime
from collections.abc import Mapping
import pytest
from ansible.module_utils.common.json import AnsibleJSONEncoder

class MockVaultObject:
    __ENCRYPTED__ = True
    _ciphertext = b'encrypted_data'

class MockUnsafeObject:
    __UNSAFE__ = True

class MockMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

def test_vault_object_to_text(monkeypatch):
    def mock_to_text(data, errors='strict', nonstring='strict'):
        return 'decrypted_data'
    
    monkeypatch.setattr('ansible.module_utils.common.json.to_text', mock_to_text)
    encoder = AnsibleJSONEncoder(vault_to_text=True)
    obj = MockVaultObject()
    result = encoder.default(obj)
    assert result == 'decrypted_data'

def test_vault_object_to_dict(monkeypatch):
    def mock_to_text(data, errors='strict', nonstring='strict'):
        return 'encrypted_data'
    
    monkeypatch.setattr('ansible.module_utils.common.json.to_text', mock_to_text)
    encoder = AnsibleJSONEncoder(vault_to_text=False)
    obj = MockVaultObject()
    result = encoder.default(obj)
    assert result == {'__ansible_vault': 'encrypted_data'}

def test_unsafe_object(monkeypatch):
    def mock_to_text(data, errors='strict', nonstring='strict'):
        return 'unsafe_data'
    
    monkeypatch.setattr('ansible.module_utils.common.json.to_text', mock_to_text)
    encoder = AnsibleJSONEncoder()
    obj = MockUnsafeObject()
    result = encoder.default(obj)
    assert result == {'__ansible_unsafe': 'unsafe_data'}

def test_mapping_object():
    encoder = AnsibleJSONEncoder()
    obj = MockMapping({'key': 'value'})
    result = encoder.default(obj)
    assert result == {'key': 'value'}

def test_date_object():
    encoder = AnsibleJSONEncoder()
    obj = datetime.date(2023, 10, 1)
    result = encoder.default(obj)
    assert result == '2023-10-01'

def test_datetime_object():
    encoder = AnsibleJSONEncoder()
    obj = datetime.datetime(2023, 10, 1, 12, 0, 0)
    result = encoder.default(obj)
    assert result == '2023-10-01T12:00:00'

def test_default_object():
    encoder = AnsibleJSONEncoder()
    obj = set([1, 2, 3])
    with pytest.raises(TypeError):
        encoder.default(obj)

def test_preprocess_unsafe(monkeypatch):
    def mock_preprocess_unsafe_encode(data):
        return 'preprocessed_data'
    
    monkeypatch.setattr('ansible.module_utils.common.json._preprocess_unsafe_encode', mock_preprocess_unsafe_encode)
    encoder = AnsibleJSONEncoder(preprocess_unsafe=True)
    obj = 'unsafe_string'
    result = list(encoder.iterencode(obj))
    assert result == ['"preprocessed_data"']
