# file: lib/ansible/parsing/yaml/objects.py:268-269
# asked: {"lines": [269], "branches": []}
# gained: {"lines": [269], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "12345"

@pytest.fixture
def encrypted_unicode():
    ciphertext = "encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_isdecimal(encrypted_unicode):
    encrypted_unicode._ciphertext = "encrypted_data"
    assert encrypted_unicode.isdecimal() == "12345".isdecimal()
