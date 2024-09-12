# file: lib/ansible/parsing/yaml/objects.py:351-352
# asked: {"lines": [352], "branches": []}
# gained: {"lines": [352], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def encrypted_unicode():
    ciphertext = b"encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_swapcase(encrypted_unicode):
    encrypted_unicode._ciphertext = b"Encrypted_Data"
    assert encrypted_unicode.swapcase() == "eNCRYPTED_dATA"
