# file: lib/ansible/parsing/yaml/objects.py:286-287
# asked: {"lines": [286, 287], "branches": []}
# gained: {"lines": [286, 287], "branches": []}

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
    obj = AnsibleVaultEncryptedUnicode(b"   ")
    obj.vault = mock_vault
    return obj

def test_isspace(encrypted_unicode):
    assert encrypted_unicode.isspace() == True

def test_not_isspace(mock_vault):
    obj = AnsibleVaultEncryptedUnicode(b"not space")
    obj.vault = mock_vault
    assert obj.isspace() == False
