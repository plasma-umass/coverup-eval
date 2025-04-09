# file: lib/ansible/parsing/yaml/objects.py:119-122
# asked: {"lines": [119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}
# gained: {"lines": [119, 120, 121, 122], "branches": [[120, 121], [120, 122]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def __init__(self, data):
        self._data = data

    def decrypt(self, ciphertext, obj):
        return self._data

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode(b"ciphertext")

def test_eq_with_vault(encrypted_unicode):
    encrypted_unicode.vault = MockVault("decrypted_data")
    assert (encrypted_unicode == "decrypted_data") is True

def test_eq_without_vault(encrypted_unicode):
    assert (encrypted_unicode == "any_data") is False
