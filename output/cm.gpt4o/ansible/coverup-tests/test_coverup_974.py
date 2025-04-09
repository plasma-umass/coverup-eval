# file lib/ansible/parsing/yaml/objects.py:218-219
# lines [218, 219]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockAnsibleBaseYAMLObject:
    def __init__(self, data):
        self._data = data
        self.vault = True  # Mocking the vault attribute

    @property
    def data(self):
        return self._data

class MockSequence:
    pass

class TestAnsibleVaultEncryptedUnicode(MockSequence, MockAnsibleBaseYAMLObject, AnsibleVaultEncryptedUnicode):
    pass

def test_ansible_vault_encrypted_unicode_mod():
    # Arrange
    data = "encrypted %s"
    obj = TestAnsibleVaultEncryptedUnicode(data)
    
    # Act
    result = obj % "data"
    
    # Assert
    assert result == "encrypted data"
