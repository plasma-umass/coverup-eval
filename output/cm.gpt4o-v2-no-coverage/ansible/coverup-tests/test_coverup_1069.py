# file: lib/ansible/parsing/yaml/objects.py:345-346
# asked: {"lines": [345, 346], "branches": []}
# gained: {"lines": [345, 346], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return "decrypted_data"

@pytest.fixture
def encrypted_unicode():
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    obj.vault = MockVault()
    return obj

def test_startswith(encrypted_unicode):
    assert encrypted_unicode.startswith("decrypted") is True
    assert encrypted_unicode.startswith("data", start=10) is True
    assert encrypted_unicode.startswith("data", start=0, end=9) is False
