# file: lib/ansible/parsing/yaml/objects.py:262-263
# asked: {"lines": [262, 263], "branches": []}
# gained: {"lines": [262, 263], "branches": []}

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
    obj = AnsibleVaultEncryptedUnicode(b"encrypted123")
    obj.vault = mock_vault
    return obj

def test_isalnum(encrypted_unicode):
    encrypted_unicode._ciphertext = b"encrypted123"
    assert encrypted_unicode.isalnum() == True

    encrypted_unicode._ciphertext = b"encrypted 123"
    assert encrypted_unicode.isalnum() == False
