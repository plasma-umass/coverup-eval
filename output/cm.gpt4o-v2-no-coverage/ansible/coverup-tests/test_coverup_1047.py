# file: lib/ansible/parsing/yaml/objects.py:228-229
# asked: {"lines": [228, 229], "branches": []}
# gained: {"lines": [228, 229], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def mock_vault():
    return MockVault()

def test_casefold(mock_vault):
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = mock_vault
    assert obj.casefold() == "decrypted_data".casefold()

def test_casefold_no_vault():
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    assert obj.casefold() == "encrypted_data".casefold()
