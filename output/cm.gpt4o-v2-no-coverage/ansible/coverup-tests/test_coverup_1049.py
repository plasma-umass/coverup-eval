# file: lib/ansible/parsing/yaml/objects.py:256-257
# asked: {"lines": [256, 257], "branches": []}
# gained: {"lines": [256, 257], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode()

@pytest.fixture
def encrypted_unicode():
    ciphertext = b"hello world"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_index(encrypted_unicode):
    assert encrypted_unicode.index("world") == 6
    assert encrypted_unicode.index("hello") == 0
    assert encrypted_unicode.index("o", 5) == 7
    with pytest.raises(ValueError):
        encrypted_unicode.index("notfound")
