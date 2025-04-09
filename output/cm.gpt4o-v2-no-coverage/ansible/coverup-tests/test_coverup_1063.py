# file: lib/ansible/parsing/yaml/objects.py:348-349
# asked: {"lines": [348, 349], "branches": []}
# gained: {"lines": [348, 349], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"encrypted_data")
    obj.vault = MockVault()
    return obj

def test_strip(encrypted_unicode):
    # Test without chars argument
    result = encrypted_unicode.strip()
    assert result == "decrypted_data".strip()

    # Test with chars argument
    result = encrypted_unicode.strip("d")
    assert result == "ecrypted_data".strip("d")
