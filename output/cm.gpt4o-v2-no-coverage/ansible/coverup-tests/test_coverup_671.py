# file: lib/ansible/parsing/yaml/objects.py:124-127
# asked: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}
# gained: {"lines": [124, 125, 126, 127], "branches": [[125, 126], [125, 127]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def __init__(self, data):
        self.data = data

    def decrypt(self, ciphertext, obj):
        return self.data

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_ne_with_vault(encrypted_unicode):
    encrypted_unicode.vault = MockVault("decrypted_data")
    assert (encrypted_unicode != "decrypted_data") is False
    assert (encrypted_unicode != "other_data") is True

def test_ne_without_vault(encrypted_unicode):
    encrypted_unicode.vault = None
    assert (encrypted_unicode != "any_data") is True
