# file: lib/ansible/parsing/yaml/objects.py:239-240
# asked: {"lines": [239, 240], "branches": []}
# gained: {"lines": [239, 240], "branches": []}

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

def test_ansible_vault_encrypted_unicode_endswith(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode(b"ciphertext")
    
    assert encrypted_unicode.endswith("text")
    assert encrypted_unicode.endswith("decrypted", 0, 9)
    assert not encrypted_unicode.endswith("ciphertext")
