# file: lib/ansible/parsing/yaml/objects.py:265-266
# asked: {"lines": [265, 266], "branches": []}
# gained: {"lines": [265, 266], "branches": []}

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

def test_isascii(mock_vault):
    encrypted_text = AnsibleVaultEncryptedUnicode("ciphertext")
    encrypted_text.vault = mock_vault
    assert encrypted_text.isascii() == "decrypted_text".isascii()

def test_cleanup(mock_vault):
    encrypted_text = AnsibleVaultEncryptedUnicode("ciphertext")
    encrypted_text.vault = mock_vault
    assert encrypted_text.isascii() == "decrypted_text".isascii()
    del encrypted_text
