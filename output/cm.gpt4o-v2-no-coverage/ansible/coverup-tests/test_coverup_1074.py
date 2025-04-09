# file: lib/ansible/parsing/yaml/objects.py:363-364
# asked: {"lines": [363, 364], "branches": []}
# gained: {"lines": [363, 364], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "12345"

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("encrypted_text")

def test_zfill(encrypted_unicode):
    encrypted_unicode.vault = MockVault()
    result = encrypted_unicode.zfill(10)
    assert result == "0000012345"
