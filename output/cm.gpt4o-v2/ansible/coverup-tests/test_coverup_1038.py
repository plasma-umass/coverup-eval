# file: lib/ansible/parsing/yaml/objects.py:225-226
# asked: {"lines": [225, 226], "branches": []}
# gained: {"lines": [225, 226], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted text"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault, monkeypatch):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    monkeypatch.setattr(obj, 'vault', mock_vault)
    monkeypatch.setattr(obj, '_ciphertext', b"ciphertext")
    return obj

def test_capitalize(encrypted_unicode):
    result = encrypted_unicode.capitalize()
    assert result == "Decrypted text"
