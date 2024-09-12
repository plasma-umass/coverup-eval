# file: lib/ansible/parsing/yaml/objects.py:304-305
# asked: {"lines": [304, 305], "branches": []}
# gained: {"lines": [304, 305], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "  decrypted data  "

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self, ciphertext, obj=None):
        return "  decrypted data  "
    monkeypatch.setattr(MockVault, "decrypt", mock_decrypt)
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = mock_vault
    return obj

def test_lstrip_no_chars(encrypted_unicode):
    result = encrypted_unicode.lstrip()
    assert result == "decrypted data  "

def test_lstrip_with_chars(encrypted_unicode):
    result = encrypted_unicode.lstrip(" d")
    assert result == "ecrypted data  "
