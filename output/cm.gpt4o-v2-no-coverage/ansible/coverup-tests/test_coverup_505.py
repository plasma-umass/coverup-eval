# file: lib/ansible/parsing/dataloader.py:129-140
# asked: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}
# gained: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    dl = DataLoader()
    dl._vault = Mock()
    return dl

@patch('ansible.parsing.dataloader.is_encrypted')
@patch('ansible.parsing.dataloader.parse_vaulttext_envelope')
def test_decrypt_if_vault_data_not_encrypted(mock_parse_vaulttext_envelope, mock_is_encrypted, dataloader):
    mock_is_encrypted.return_value = False
    b_vault_data = b"unencrypted data"
    
    result, show_content = dataloader._decrypt_if_vault_data(b_vault_data)
    
    assert result == b_vault_data
    assert show_content is True
    mock_is_encrypted.assert_called_once_with(b_vault_data)
    mock_parse_vaulttext_envelope.assert_not_called()

@patch('ansible.parsing.dataloader.is_encrypted')
@patch('ansible.parsing.dataloader.parse_vaulttext_envelope')
def test_decrypt_if_vault_data_encrypted(mock_parse_vaulttext_envelope, mock_is_encrypted, dataloader):
    mock_is_encrypted.return_value = True
    b_vault_data = b"$ANSIBLE_VAULT;1.1;AES256\n..."
    b_ciphertext = b"ciphertext"
    b_version = b"1.1"
    cipher_name = "AES256"
    vault_id = "default"
    
    mock_parse_vaulttext_envelope.return_value = (b_ciphertext, b_version, cipher_name, vault_id)
    dataloader._vault.decrypt.return_value = b"decrypted data"
    
    result, show_content = dataloader._decrypt_if_vault_data(b_vault_data)
    
    assert result == b"decrypted data"
    assert show_content is False
    mock_is_encrypted.assert_called_once_with(b_vault_data)
    mock_parse_vaulttext_envelope.assert_called_once_with(b_vault_data)
    dataloader._vault.decrypt.assert_called_once_with(b_vault_data, filename=None)
