# file: lib/ansible/parsing/yaml/objects.py:280-281
# asked: {"lines": [281], "branches": []}
# gained: {"lines": [281], "branches": []}

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
    obj = AnsibleVaultEncryptedUnicode(b'12345')
    obj.vault = mock_vault
    return obj

def test_isnumeric(encrypted_unicode):
    assert encrypted_unicode.isnumeric() == True

def test_isnumeric_non_numeric(monkeypatch, encrypted_unicode):
    def mock_decrypt(self, ciphertext, obj=None):
        return 'abcde'
    
    monkeypatch.setattr(MockVault, 'decrypt', mock_decrypt)
    assert encrypted_unicode.isnumeric() == False
