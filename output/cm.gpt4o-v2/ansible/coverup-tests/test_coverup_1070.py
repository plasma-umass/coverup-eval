# file: lib/ansible/parsing/yaml/objects.py:339-340
# asked: {"lines": [339, 340], "branches": []}
# gained: {"lines": [339, 340], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_rsplit(encrypted_unicode):
    result = encrypted_unicode.rsplit()
    assert result == ["decrypted", "data"], "rsplit() did not return the expected result"

    result = encrypted_unicode.rsplit(' ', 1)
    assert result == ["decrypted", "data"], "rsplit(' ', 1) did not return the expected result"
