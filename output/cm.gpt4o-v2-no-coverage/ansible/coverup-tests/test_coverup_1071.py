# file: lib/ansible/parsing/yaml/objects.py:262-263
# asked: {"lines": [262, 263], "branches": []}
# gained: {"lines": [262, 263], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def __init__(self, data):
        self.data = data

    def decrypt(self, ciphertext, obj=None):
        return self.data

@pytest.fixture
def mock_vault():
    return MockVault("decrypteddata123")

def test_isalnum(mock_vault, monkeypatch):
    encrypted_text = AnsibleVaultEncryptedUnicode("encrypted_data")
    monkeypatch.setattr(encrypted_text, 'vault', mock_vault)
    monkeypatch.setattr(encrypted_text, '_ciphertext', b"encrypted_data")
    
    assert encrypted_text.isalnum() == True

    mock_vault.data = "decrypted data 123"
    assert encrypted_text.isalnum() == False
