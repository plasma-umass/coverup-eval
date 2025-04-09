# file: lib/ansible/parsing/yaml/objects.py:277-278
# asked: {"lines": [277, 278], "branches": []}
# gained: {"lines": [277, 278], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_unicode(mock_vault):
    obj = AnsibleVaultEncryptedUnicode("encrypted_text")
    obj.vault = mock_vault
    return obj

def test_islower(encrypted_unicode):
    encrypted_unicode.vault.decrypt = lambda x, obj=None: "lowercase"
    assert encrypted_unicode.islower() == True

    encrypted_unicode.vault.decrypt = lambda x, obj=None: "UPPERCASE"
    assert encrypted_unicode.islower() == False

def test_cleanup(encrypted_unicode):
    encrypted_unicode.vault = None
    assert encrypted_unicode.vault is None
