# file: lib/ansible/parsing/yaml/objects.py:271-272
# asked: {"lines": [271, 272], "branches": []}
# gained: {"lines": [271, 272], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext

@pytest.fixture
def mock_vault(monkeypatch):
    def mock_decrypt(self, ciphertext, obj=None):
        return ciphertext
    monkeypatch.setattr(MockVault, 'decrypt', mock_decrypt)

def test_isdigit(mock_vault):
    encrypted_unicode = AnsibleVaultEncryptedUnicode("12345")
    encrypted_unicode.vault = MockVault()
    assert encrypted_unicode.isdigit() == True

    encrypted_unicode = AnsibleVaultEncryptedUnicode("123a45")
    encrypted_unicode.vault = MockVault()
    assert encrypted_unicode.isdigit() == False
