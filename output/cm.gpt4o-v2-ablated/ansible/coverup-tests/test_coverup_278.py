# file: lib/ansible/parsing/yaml/objects.py:92-104
# asked: {"lines": [92, 100, 103, 104], "branches": []}
# gained: {"lines": [92, 100, 103, 104], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.module_utils._text import to_bytes

class MockVault:
    def decrypt(self, ciphertext):
        return b"decrypted_text"

@pytest.fixture
def mock_vault():
    return MockVault()

def test_ansible_vault_encrypted_unicode_init():
    ciphertext = "encrypted_text"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert obj._ciphertext == to_bytes(ciphertext)
    assert obj.vault is None

def test_ansible_vault_encrypted_unicode_decrypt(mock_vault):
    ciphertext = "encrypted_text"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = mock_vault
    assert obj.vault.decrypt(obj._ciphertext) == b"decrypted_text"
