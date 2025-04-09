# file: lib/ansible/parsing/yaml/objects.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "DECRYPTED_TEXT"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_init(self, ciphertext):
        self.vault = MockVault()
        self._ciphertext = ciphertext

    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "__init__", mock_init)

def test_ansible_vault_encrypted_unicode_lower(mock_vault, monkeypatch):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("ciphertext")
    assert encrypted_unicode.vault is not None
    assert encrypted_unicode._ciphertext == "ciphertext"
    
    # Mock the data property to return a known value
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "data", "DECRYPTED_TEXT")
    
    assert encrypted_unicode.lower() == "decrypted_text".lower()
