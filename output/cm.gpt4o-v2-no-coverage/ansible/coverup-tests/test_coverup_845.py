# file: lib/ansible/parsing/yaml/objects.py:112-114
# asked: {"lines": [112, 113, 114], "branches": []}
# gained: {"lines": [112, 113, 114], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return b"decrypted_" + ciphertext

def test_ansible_vault_encrypted_unicode_data_setter():
    obj = AnsibleVaultEncryptedUnicode(b"initial_ciphertext")
    new_value = "new_ciphertext"
    obj.data = new_value
    assert obj._ciphertext == to_bytes(new_value)

def test_ansible_vault_encrypted_unicode_data_getter_no_vault():
    obj = AnsibleVaultEncryptedUnicode(b"initial_ciphertext")
    assert obj.data == "initial_ciphertext"

def test_ansible_vault_encrypted_unicode_data_getter_with_vault():
    obj = AnsibleVaultEncryptedUnicode(b"initial_ciphertext")
    obj.vault = MockVault()
    assert obj.data == "decrypted_initial_ciphertext"
