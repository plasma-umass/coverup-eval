# file: lib/ansible/parsing/yaml/objects.py:298-299
# asked: {"lines": [298, 299], "branches": []}
# gained: {"lines": [298, 299], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    vault = MockVault()
    ciphertext = "ciphertext"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = vault
    return obj

def test_ljust(encrypted_unicode):
    result = encrypted_unicode.ljust(20)
    assert result == "decrypted_data".ljust(20)
