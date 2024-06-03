# file lib/ansible/parsing/yaml/objects.py:146-147
# lines [147]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data, vault=None):
        self._data = data
        self.vault = vault

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_repr():
    mock_data = "mock_encrypted_data"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data, vault=True)
    assert repr(obj) == repr(mock_data)
