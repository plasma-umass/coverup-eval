# file lib/ansible/parsing/yaml/objects.py:124-127
# lines [124, 125, 126, 127]
# branches ['125->126', '125->127']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode

@pytest.fixture
def mock_vault(mocker):
    mock = mocker.MagicMock()
    mock.decrypt.return_value = 'encrypted_data'
    return mock

def test_ansible_vault_encrypted_unicode_ne_with_vault(mock_vault):
    vault_encrypted_unicode = AnsibleVaultEncryptedUnicode('ciphertext')
    vault_encrypted_unicode.vault = mock_vault
    vault_encrypted_unicode.data = 'encrypted_data'

    assert (vault_encrypted_unicode != 'encrypted_data') is False
    assert (vault_encrypted_unicode != 'other_data') is True

def test_ansible_vault_encrypted_unicode_ne_without_vault():
    vault_encrypted_unicode = AnsibleVaultEncryptedUnicode('ciphertext')
    vault_encrypted_unicode.vault = None

    assert (vault_encrypted_unicode != 'any_data') is True
