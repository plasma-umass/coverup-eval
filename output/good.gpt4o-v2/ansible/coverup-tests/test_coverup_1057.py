# file: lib/ansible/parsing/yaml/objects.py:239-240
# asked: {"lines": [239, 240], "branches": []}
# gained: {"lines": [239, 240], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_data(self):
        return "decrypted_data"
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_data))

def test_ansible_vault_encrypted_unicode_endswith(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("ciphertext")
    
    assert encrypted_unicode.endswith("data")
    assert not encrypted_unicode.endswith("wrong_suffix")
    assert encrypted_unicode.endswith("crypted_data", 2, 14)
