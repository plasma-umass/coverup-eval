# file: lib/ansible/parsing/yaml/objects.py:106-110
# asked: {"lines": [106, 107, 108, 109, 110], "branches": [[108, 109], [108, 110]]}
# gained: {"lines": [106, 107, 108, 109, 110], "branches": [[108, 109], [108, 110]]}

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from unittest.mock import Mock, patch

@pytest.fixture
def mock_vault():
    return Mock()

@pytest.fixture
def encrypted_unicode_no_vault():
    obj = AnsibleVaultEncryptedUnicode(ciphertext=b'some_ciphertext')
    obj.vault = None
    return obj

@pytest.fixture
def encrypted_unicode_with_vault(mock_vault):
    obj = AnsibleVaultEncryptedUnicode(ciphertext=b'some_ciphertext')
    obj.vault = mock_vault
    return obj

def test_data_property_no_vault(encrypted_unicode_no_vault):
    result = encrypted_unicode_no_vault.data
    assert result == 'some_ciphertext'

def test_data_property_with_vault(encrypted_unicode_with_vault, mock_vault):
    mock_vault.decrypt.return_value = b'decrypted_text'
    result = encrypted_unicode_with_vault.data
    mock_vault.decrypt.assert_called_once_with(b'some_ciphertext', obj=encrypted_unicode_with_vault)
    assert result == 'decrypted_text'
