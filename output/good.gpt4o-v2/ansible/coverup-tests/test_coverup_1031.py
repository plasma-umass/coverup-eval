# file: lib/ansible/parsing/yaml/objects.py:213-214
# asked: {"lines": [213, 214], "branches": []}
# gained: {"lines": [213, 214], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode("ciphertext")
    obj.vault = MockVault()
    return obj

def test_mul(encrypted_unicode):
    result = encrypted_unicode * 3
    assert result == "decrypted_data" * 3
