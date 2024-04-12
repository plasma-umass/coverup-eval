# file lib/ansible/parsing/yaml/objects.py:106-110
# lines [106, 107, 108, 109, 110]
# branches ['108->109', '108->110']

import pytest
from ansible.parsing.yaml.objects import AnsibleVaultEncryptedUnicode
from ansible.parsing.vault import VaultLib

@pytest.fixture
def mock_vault(mocker):
    vault = mocker.MagicMock(spec=VaultLib)
    vault.decrypt.return_value = b'decrypted_value'
    return vault

@pytest.fixture
def vault_encrypted_unicode(mock_vault):
    avu = AnsibleVaultEncryptedUnicode(ciphertext=b'encrypted_value')
    avu.vault = mock_vault
    return avu

def test_ansible_vault_encrypted_unicode_without_vault():
    avu = AnsibleVaultEncryptedUnicode(ciphertext=b'encrypted_value')
    avu.vault = None
    assert avu.data == 'encrypted_value'

def test_ansible_vault_encrypted_unicode_with_vault(vault_encrypted_unicode, mock_vault):
    assert vault_encrypted_unicode.data == 'decrypted_value'
    mock_vault.decrypt.assert_called_once_with(b'encrypted_value', obj=vault_encrypted_unicode)
