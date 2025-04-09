# file: lib/ansible/parsing/yaml/objects.py:298-299
# asked: {"lines": [298, 299], "branches": []}
# gained: {"lines": [298, 299], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_init(self, ciphertext):
        self.vault = MockVault()
        self._ciphertext = ciphertext

    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "__init__", mock_init)

def test_ljust(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("ciphertext")
    result = encrypted_unicode.ljust(20)
    assert result == "decrypted_text".ljust(20)
