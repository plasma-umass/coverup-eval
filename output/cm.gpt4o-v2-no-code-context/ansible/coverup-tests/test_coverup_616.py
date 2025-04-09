# file: lib/ansible/parsing/yaml/objects.py:92-104
# asked: {"lines": [92, 100, 103, 104], "branches": []}
# gained: {"lines": [92, 100, 103, 104], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultLib

def test_ansible_vault_encrypted_unicode_init():
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    
    assert obj.vault is None
    assert obj._ciphertext == ciphertext

def test_ansible_vault_encrypted_unicode_with_vault(monkeypatch):
    ciphertext = b"encrypted_data"
    decrypted_data = "decrypted_data"
    
    class MockVaultLib:
        def decrypt(self, data):
            return decrypted_data
    
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVaultLib()
    
    assert obj.vault.decrypt(obj._ciphertext) == decrypted_data
