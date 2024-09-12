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
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_getitem(encrypted_unicode):
    encrypted_unicode.data = "decrypted_data"
    assert encrypted_unicode[0] == "d"
    assert encrypted_unicode[:4] == "decr"
    assert encrypted_unicode[-1] == "a"
