# file: lib/ansible/parsing/yaml/objects.py:218-219
# asked: {"lines": [218, 219], "branches": []}
# gained: {"lines": [218, 219], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted_data"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self):
        return "decrypted %s"
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_decrypt))

def test_ansible_vault_encrypted_unicode_mod(mock_vault):
    encrypted = AnsibleVaultEncryptedUnicode("ciphertext")
    result = encrypted % "data"
    assert result == "decrypted data"
