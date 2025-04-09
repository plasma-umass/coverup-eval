# file: lib/ansible/parsing/yaml/objects.py:116-117
# asked: {"lines": [116, 117], "branches": []}
# gained: {"lines": [116, 117], "branches": []}

import pytest
from unittest.mock import Mock
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def mock_vault():
    return Mock()

def test_is_encrypted_with_encrypted_vault(mock_vault):
    mock_vault.is_encrypted.return_value = True
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    obj.vault = mock_vault
    assert obj.is_encrypted() is True

def test_is_encrypted_with_non_encrypted_vault(mock_vault):
    mock_vault.is_encrypted.return_value = False
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    obj.vault = mock_vault
    assert obj.is_encrypted() is False

def test_is_encrypted_with_no_vault():
    obj = AnsibleVaultEncryptedUnicode(b"ciphertext")
    assert obj.is_encrypted() is None
