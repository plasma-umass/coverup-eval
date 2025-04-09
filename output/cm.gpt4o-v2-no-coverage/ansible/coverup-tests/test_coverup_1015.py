# file: lib/ansible/parsing/yaml/objects.py:149-150
# asked: {"lines": [149, 150], "branches": []}
# gained: {"lines": [149, 150], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_int():
    # Create an instance of AnsibleVaultEncryptedUnicode with mock ciphertext
    ciphertext = "12345"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    # Mock the data property to return a specific value
    obj.data = "12345"
    
    # Test the __int__ method
    result = int(obj)
    
    # Assert the result is as expected
    assert result == 12345

    # Clean up
    del obj
