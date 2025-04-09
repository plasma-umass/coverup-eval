# file: lib/ansible/parsing/yaml/objects.py:213-214
# asked: {"lines": [213, 214], "branches": []}
# gained: {"lines": [213, 214], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    def test_mul(self):
        # Arrange
        ciphertext = "encrypted_data"
        obj = AnsibleVaultEncryptedUnicode(ciphertext)
        
        # Act
        result = obj * 3
        
        # Assert
        assert result == obj.data * 3

    def test_rmul(self):
        # Arrange
        ciphertext = "encrypted_data"
        obj = AnsibleVaultEncryptedUnicode(ciphertext)
        
        # Act
        result = 3 * obj
        
        # Assert
        assert result == obj.data * 3
