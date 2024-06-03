# file lib/ansible/parsing/yaml/objects.py:298-299
# lines [299]
# branches []

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

def test_ansible_vault_encrypted_unicode_ljust():
    # Mock the data attribute to be a string
    obj = AnsibleVaultEncryptedUnicode(ciphertext="dummy_ciphertext")
    obj.data = "test"

    # Call the ljust method and assert the result
    result = obj.ljust(10)
    assert result == "test      "

    # Call the ljust method with fillchar and assert the result
    result = obj.ljust(10, '*')
    assert result == "test******"
