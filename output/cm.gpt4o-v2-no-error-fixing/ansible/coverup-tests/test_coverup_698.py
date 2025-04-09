# file: lib/ansible/parsing/yaml/objects.py:129-132
# asked: {"lines": [129, 132], "branches": []}
# gained: {"lines": [129, 132], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_text

def test_ansible_vault_encrypted_unicode_reversed():
    # Create an instance of AnsibleVaultEncryptedUnicode with some ciphertext
    ciphertext = b"encryptedtext"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    # Call the __reversed__ method
    reversed_obj = obj.__reversed__()
    
    # Verify the result
    assert reversed_obj == to_text(ciphertext[::-1], errors='surrogate_or_strict')
