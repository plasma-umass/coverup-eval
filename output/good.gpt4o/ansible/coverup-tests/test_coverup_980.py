# file lib/ansible/parsing/yaml/objects.py:231-232
# lines [231, 232]
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

def test_ansible_vault_encrypted_unicode_center():
    mock_data = "encrypted_data"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    centered_data = obj.center(20)
    
    assert centered_data == mock_data.center(20)
