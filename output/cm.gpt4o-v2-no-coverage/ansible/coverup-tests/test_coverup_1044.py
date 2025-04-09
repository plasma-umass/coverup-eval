# file: lib/ansible/parsing/yaml/objects.py:193-194
# asked: {"lines": [193, 194], "branches": []}
# gained: {"lines": [193, 194], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    vault = MockVault()
    obj = AnsibleVaultEncryptedUnicode("encrypted_data")
    obj.vault = vault
    return obj

def test_getitem(encrypted_unicode):
    assert encrypted_unicode[0] == "d"
    assert encrypted_unicode[:4] == "decr"
    assert encrypted_unicode[-1] == "a"
