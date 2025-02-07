# file: lib/ansible/parsing/yaml/objects.py:357-358
# asked: {"lines": [358], "branches": []}
# gained: {"lines": [358], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext):
        return "decrypted text"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = mock_vault
    return obj

def test_translate(monkeypatch, encrypted_unicode):
    def mock_data(self):
        return "decrypted text"
    
    monkeypatch.setattr(AnsibleVaultEncryptedUnicode, 'data', property(mock_data))
    
    result = encrypted_unicode.translate(str.maketrans("decrypted text", "DECRYPTED TEXT"))
    assert result == "DECRYPTED TEXT"
