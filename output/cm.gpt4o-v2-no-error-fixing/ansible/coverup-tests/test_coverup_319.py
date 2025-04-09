# file: lib/ansible/parsing/dataloader.py:129-140
# asked: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}
# gained: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}

import pytest
from unittest.mock import Mock, patch
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import is_encrypted, parse_vaulttext_envelope

class TestDataLoader:

    @patch('ansible.parsing.dataloader.is_encrypted')
    @patch('ansible.parsing.dataloader.parse_vaulttext_envelope')
    def test_decrypt_if_vault_data_not_encrypted(self, mock_parse_vaulttext_envelope, mock_is_encrypted):
        mock_is_encrypted.return_value = False
        data_loader = DataLoader()
        b_vault_data = b'not encrypted data'
        
        result, show_content = data_loader._decrypt_if_vault_data(b_vault_data)
        
        assert result == b_vault_data
        assert show_content is True
        mock_is_encrypted.assert_called_once_with(b_vault_data)
        mock_parse_vaulttext_envelope.assert_not_called()

    @patch('ansible.parsing.dataloader.is_encrypted')
    @patch('ansible.parsing.dataloader.parse_vaulttext_envelope')
    def test_decrypt_if_vault_data_encrypted(self, mock_parse_vaulttext_envelope, mock_is_encrypted):
        mock_is_encrypted.return_value = True
        mock_parse_vaulttext_envelope.return_value = (b'ciphertext', b'version', 'cipher_name', 'vault_id')
        mock_vault = Mock()
        mock_vault.decrypt.return_value = b'decrypted data'
        
        data_loader = DataLoader()
        data_loader._vault = mock_vault
        b_vault_data = b'$ANSIBLE_VAULT;1.1;AES256\n'
        
        result, show_content = data_loader._decrypt_if_vault_data(b_vault_data)
        
        assert result == b'decrypted data'
        assert show_content is False
        mock_is_encrypted.assert_called_once_with(b_vault_data)
        mock_parse_vaulttext_envelope.assert_called_once_with(b_vault_data)
        mock_vault.decrypt.assert_called_once_with(b_vault_data, filename=None)
