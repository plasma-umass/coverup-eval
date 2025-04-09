# file lib/ansible/parsing/yaml/objects.py:363-364
# lines [364]
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

def test_ansible_vault_encrypted_unicode_zfill():
    mock_data = "12345"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    result = obj.zfill(10)
    
    assert result == mock_data.zfill(10)
