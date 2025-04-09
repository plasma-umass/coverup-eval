# file: lib/ansible/parsing/yaml/objects.py:134-135
# asked: {"lines": [134, 135], "branches": []}
# gained: {"lines": [134, 135], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_native

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Ensure the vault attribute is set to avoid AttributeError

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_str(monkeypatch):
    # Mock data to ensure the __str__ method is called
    mock_data = b'some encrypted data'
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)

    # Mock the to_native function to ensure it is called with the correct parameters
    def mock_to_native(data, errors):
        assert data == mock_data
        assert errors == 'surrogate_or_strict'
        return 'mocked native string'

    monkeypatch.setattr('ansible.parsing.yaml.objects.to_native', mock_to_native)

    # Call the __str__ method and verify the result
    result = obj.__str__()
    assert result == 'mocked native string'
