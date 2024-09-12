# file: lib/ansible/parsing/yaml/objects.py:301-302
# asked: {"lines": [301, 302], "branches": []}
# gained: {"lines": [301, 302], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    vault = MockVault()
    obj = AnsibleVaultEncryptedUnicode("encrypted_data")
    obj.vault = vault
    return obj

def test_lower(encrypted_unicode):
    assert encrypted_unicode.lower() == "decrypted_data".lower()
