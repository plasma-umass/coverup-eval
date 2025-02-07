# file: lib/ansible/parsing/yaml/objects.py:324-325
# asked: {"lines": [324, 325], "branches": []}
# gained: {"lines": [324, 325], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted text"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_rindex(encrypted_unicode):
    assert encrypted_unicode.rindex("text") == 10
    assert encrypted_unicode.rindex("decrypted") == 0
    with pytest.raises(ValueError):
        encrypted_unicode.rindex("notfound")
