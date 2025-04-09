# file: lib/ansible/parsing/yaml/objects.py:190-191
# asked: {"lines": [190, 191], "branches": []}
# gained: {"lines": [190, 191], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def mock_vault():
    return MockVault()

def test_ansible_vault_encrypted_unicode_len(mock_vault, monkeypatch):
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    monkeypatch.setattr(obj, 'vault', mock_vault)
    monkeypatch.setattr(obj, '_ciphertext', ciphertext)
    
    assert len(obj) == len("decrypted_data")
