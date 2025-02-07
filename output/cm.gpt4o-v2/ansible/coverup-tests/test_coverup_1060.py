# file: lib/ansible/parsing/yaml/objects.py:265-266
# asked: {"lines": [265, 266], "branches": []}
# gained: {"lines": [265, 266], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode(b"test")
    obj.vault = mock_vault
    return obj

def test_isascii(encrypted_unicode):
    assert encrypted_unicode.isascii() == True

def test_isascii_non_ascii(monkeypatch, encrypted_unicode):
    def mock_decrypt(self, ciphertext, obj=None):
        return "tëst"
    
    monkeypatch.setattr(MockVault, "decrypt", mock_decrypt)
    assert encrypted_unicode.isascii() == False
