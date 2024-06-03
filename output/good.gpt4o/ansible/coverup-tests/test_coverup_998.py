# file lib/ansible/parsing/yaml/objects.py:301-302
# lines [301, 302]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_lower():
    mock_data = "ENCRYPTEDDATA"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    assert obj.lower() == mock_data.lower()
