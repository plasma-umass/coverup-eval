# file: lib/ansible/parsing/yaml/objects.py:330-331
# asked: {"lines": [330, 331], "branches": []}
# gained: {"lines": [330, 331], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class TestAnsibleVaultEncryptedUnicode:
    
    def test_rpartition(self):
        # Arrange
        ciphertext = "encrypted_data"
        obj = AnsibleVaultEncryptedUnicode(ciphertext)
        obj.data = "some_data_to_partition"
        
        # Act
        result = obj.rpartition("_to_")
        
        # Assert
        assert result == ("some_data", "_to_", "partition")
        
        # Clean up
        del obj
