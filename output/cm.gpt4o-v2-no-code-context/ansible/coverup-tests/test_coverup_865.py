# file: lib/ansible/parsing/yaml/objects.py:146-147
# asked: {"lines": [146, 147], "branches": []}
# gained: {"lines": [146, 147], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_repr():
    mock_data = "encrypted_data"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    assert repr(obj) == repr(mock_data)
