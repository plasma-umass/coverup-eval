# file: lib/ansible/parsing/yaml/objects.py:327-328
# asked: {"lines": [328], "branches": []}
# gained: {"lines": [328], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    ciphertext = "mock_ciphertext"
    obj = AnsibleVaultEncryptedUnicode(ciphertext)
    obj.vault = MockVault()
    return obj

def test_rjust(encrypted_unicode):
    result = encrypted_unicode.rjust(20)
    assert result == "decrypted_data".rjust(20)
