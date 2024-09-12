# file: lib/ansible/parsing/yaml/objects.py:256-257
# asked: {"lines": [256, 257], "branches": []}
# gained: {"lines": [256, 257], "branches": []}

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

def test_index_method(encrypted_unicode):
    assert encrypted_unicode.index("decrypted") == 0
    assert encrypted_unicode.index("data") == 10
    assert encrypted_unicode.index("data", 5) == 10
    assert encrypted_unicode.index("data", 0, 15) == 10

    with pytest.raises(ValueError):
        encrypted_unicode.index("not_in_data")
