# file: lib/ansible/parsing/yaml/objects.py:354-355
# asked: {"lines": [354, 355], "branches": []}
# gained: {"lines": [354, 355], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted text"

@pytest.fixture
def encrypted_unicode():
    ciphertext = "encrypted text"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_title_method(encrypted_unicode):
    assert encrypted_unicode.title() == "decrypted text".title()
