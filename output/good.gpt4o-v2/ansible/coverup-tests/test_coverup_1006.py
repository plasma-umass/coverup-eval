# file: lib/ansible/parsing/yaml/objects.py:155-156
# asked: {"lines": [155, 156], "branches": []}
# gained: {"lines": [155, 156], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_complex():
    # Create an instance of AnsibleVaultEncryptedUnicode with a valid ciphertext
    ciphertext = "3.14"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    # Mock the data property to return a string that can be converted to a complex number
    obj.data = "3.14"
    
    # Verify that __complex__ method returns the correct complex number
    assert complex(obj) == complex("3.14")
