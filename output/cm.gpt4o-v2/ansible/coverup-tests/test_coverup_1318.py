# file: lib/ansible/parsing/yaml/objects.py:330-331
# asked: {"lines": [331], "branches": []}
# gained: {"lines": [331], "branches": []}

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

def test_rpartition(encrypted_unicode):
    result = encrypted_unicode.rpartition("c")
    assert result == ("de", "c", "rypted_data")
