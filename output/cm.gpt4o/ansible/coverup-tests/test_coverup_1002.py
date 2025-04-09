# file lib/ansible/parsing/yaml/objects.py:330-331
# lines [330, 331]
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

def test_ansible_vault_encrypted_unicode_rpartition():
    mock_data = "vaulted_data"
    sep = "_"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    result = obj.rpartition(sep)
    
    assert result == ("vaulted", "_", "data")
