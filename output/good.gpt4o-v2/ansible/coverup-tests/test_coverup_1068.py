# file: lib/ansible/parsing/yaml/objects.py:360-361
# asked: {"lines": [360, 361], "branches": []}
# gained: {"lines": [360, 361], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    ciphertext = "encrypted_data"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_upper(encrypted_unicode):
    assert encrypted_unicode.upper() == "DECRYPTED_DATA"
