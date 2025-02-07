# file: lib/ansible/parsing/yaml/objects.py:116-117
# asked: {"lines": [116, 117], "branches": []}
# gained: {"lines": [116, 117], "branches": []}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def is_encrypted(self, ciphertext):
        return True

@pytest.fixture
def encrypted_unicode():
    return AnsibleVaultEncryptedUnicode("ciphertext")

def test_is_encrypted_true(encrypted_unicode, mocker):
    mock_vault = MockVault()
    encrypted_unicode.vault = mock_vault
    assert encrypted_unicode.is_encrypted() is True

def test_is_encrypted_false(encrypted_unicode):
    encrypted_unicode.vault = None
    assert encrypted_unicode.is_encrypted() is None
