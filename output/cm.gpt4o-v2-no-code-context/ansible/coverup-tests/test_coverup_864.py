# file: lib/ansible/parsing/yaml/objects.py:190-191
# asked: {"lines": [190, 191], "branches": []}
# gained: {"lines": [190, 191], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mocking the vault attribute to avoid AttributeError

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_len():
    mock_data = "encrypted_data"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    assert len(obj) == len(mock_data)
