# file: lib/ansible/parsing/yaml/objects.py:225-226
# asked: {"lines": [225, 226], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self, ciphertext, obj=None):
        return "decrypted_text"
    monkeypatch.setattr(MockVault, "decrypt", mock_decrypt)
    return MockVault()

def test_ansible_vault_encrypted_unicode_capitalize(mock_vault):
    encrypted_text = AnsibleVaultEncryptedUnicode("encrypted_text")
    encrypted_text.vault = mock_vault
    assert encrypted_text.capitalize() == "Decrypted_text"
