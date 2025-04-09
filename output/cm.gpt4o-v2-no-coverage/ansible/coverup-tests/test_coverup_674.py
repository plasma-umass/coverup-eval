# file: lib/ansible/parsing/yaml/objects.py:180-183
# asked: {"lines": [180, 181, 182, 183], "branches": [[181, 182], [181, 183]]}
# gained: {"lines": [180, 181, 182, 183], "branches": [[181, 182], [181, 183]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

class MockVault:
    def decrypt(self, ciphertext, obj=None):
        return ciphertext.decode('utf-8')

@pytest.fixture
def mock_vault():
    return MockVault()

@pytest.fixture
def encrypted_string(mock_vault):
    obj = AnsibleVaultEncryptedUnicode(b"encrypted_data")
    obj.vault = mock_vault
    return obj

def test_ge_with_same_type(encrypted_string):
    other = AnsibleVaultEncryptedUnicode(b"other_encrypted_data")
    other.vault = encrypted_string.vault
    assert (encrypted_string >= other) == (encrypted_string.data >= other.data)

def test_ge_with_string(encrypted_string):
    assert (encrypted_string >= "plain_string") == (encrypted_string.data >= "plain_string")

def test_ge_with_different_type(encrypted_string):
    with pytest.raises(TypeError):
        encrypted_string >= 123

def test_ge_with_none(encrypted_string):
    with pytest.raises(TypeError):
        encrypted_string >= None

def test_ge_with_empty_string(encrypted_string):
    assert (encrypted_string >= "") == (encrypted_string.data >= "")

def test_ge_with_non_empty_string(encrypted_string):
    assert (encrypted_string >= "non_empty_string") == (encrypted_string.data >= "non_empty_string")
