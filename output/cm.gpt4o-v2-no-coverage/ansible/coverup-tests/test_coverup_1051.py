# file: lib/ansible/parsing/yaml/objects.py:309-310
# asked: {"lines": [309, 310], "branches": []}
# gained: {"lines": [309, 310], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_text"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_partition(encrypted_unicode):
    result = encrypted_unicode.partition("e")
    assert result == ("d", "e", "crypted_text")
