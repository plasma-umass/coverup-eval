# file: lib/ansible/parsing/yaml/objects.py:196-199
# asked: {"lines": [196, 197, 198, 199], "branches": []}
# gained: {"lines": [196, 197, 198, 199], "branches": []}

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

def test_getslice(encrypted_unicode):
    encrypted_unicode.data = "decrypted_data"
    result = encrypted_unicode.__getslice__(-5, 5)
    assert result == "decry"
