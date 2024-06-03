# file lib/ansible/parsing/yaml/objects.py:225-226
# lines [225, 226]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleVaultEncryptedUnicode(AnsibleVaultEncryptedUnicode):
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mocking the vault attribute

    @property
    def data(self):
        return self._data

def test_ansible_vault_encrypted_unicode_capitalize():
    # Arrange
    mock_data = "encryptedstring"
    obj = MockAnsibleVaultEncryptedUnicode(mock_data)
    
    # Act
    result = obj.capitalize()
    
    # Assert
    assert result == mock_data.capitalize()
