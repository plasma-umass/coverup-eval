# file: lib/ansible/parsing/yaml/objects.py:112-114
# asked: {"lines": [112, 113, 114], "branches": []}
# gained: {"lines": [112, 113, 114], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

def test_ansible_vault_encrypted_unicode_data_setter():
    # Create an instance of AnsibleVaultEncryptedUnicode with required argument
    test_ciphertext = "initial_ciphertext"
    encrypted_unicode = AnsibleVaultEncryptedUnicode(test_ciphertext)

    # Set the data attribute to trigger the setter
    test_value = "test_value"
    encrypted_unicode.data = test_value

    # Verify that the _ciphertext attribute is correctly set
    assert encrypted_unicode._ciphertext == to_bytes(test_value)
