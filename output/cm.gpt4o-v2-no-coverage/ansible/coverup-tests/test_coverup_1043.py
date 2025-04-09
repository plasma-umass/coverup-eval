# file: lib/ansible/parsing/yaml/objects.py:289-290
# asked: {"lines": [289, 290], "branches": []}
# gained: {"lines": [289, 290], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "Decrypted Text"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_init(self, ciphertext):
        self.vault = MockVault()
        self._ciphertext = ciphertext
    
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "__init__", mock_init)
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, "data", property(lambda self: self.vault.decrypt(self._ciphertext)))

def test_ansible_vault_encrypted_unicode_istitle(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("ciphertext")
    assert encrypted_unicode.istitle() == "Decrypted Text".istitle()
