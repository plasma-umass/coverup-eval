# file: lib/ansible/parsing/yaml/objects.py:112-114
# asked: {"lines": [112, 113, 114], "branches": []}
# gained: {"lines": [112, 113, 114], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

def test_ansible_vault_encrypted_unicode_data_setter():
    # Create an instance of AnsibleVaultEncryptedUnicode
    encrypted_unicode = AnsibleVaultEncryptedUnicode("ciphertext")

    # Set new data
    new_data = "new_ciphertext"
    encrypted_unicode.data = new_data

    # Assert that the _ciphertext attribute is updated correctly
    assert encrypted_unicode._ciphertext == to_bytes(new_data)
