# file: lib/ansible/parsing/yaml/objects.py:146-147
# asked: {"lines": [146, 147], "branches": []}
# gained: {"lines": [146, 147], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_repr():
    # Create an instance of AnsibleVaultEncryptedUnicode with some ciphertext
    ciphertext = "encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    # Mock the data property to return a specific value
    obj.data = "decrypted_data"
    
    # Check the __repr__ method
    assert repr(obj) == repr("decrypted_data")
