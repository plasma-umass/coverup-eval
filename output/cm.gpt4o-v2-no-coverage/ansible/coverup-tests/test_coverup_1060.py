# file: lib/ansible/parsing/yaml/objects.py:360-361
# asked: {"lines": [360, 361], "branches": []}
# gained: {"lines": [360, 361], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_upper():
    # Arrange
    ciphertext = "encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    # Mock the data property to return a known value
    obj.data = "decrypted_data"
    
    # Act
    result = obj.upper()
    
    # Assert
    assert result == "DECRYPTED_DATA"

