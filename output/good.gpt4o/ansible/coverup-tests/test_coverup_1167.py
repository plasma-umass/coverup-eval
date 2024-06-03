# file lib/ansible/parsing/dataloader.py:129-140
# lines [132, 133, 134, 136, 137, 139, 140]
# branches ['132->133', '132->136']

import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_decrypt_if_vault_data_not_encrypted(dataloader):
    with patch('ansible.parsing.dataloader.is_encrypted', return_value=False):
        b_vault_data = b"not encrypted data"
        b_data, show_content = dataloader._decrypt_if_vault_data(b_vault_data)
        assert b_data == b_vault_data
        assert show_content is True

def test_decrypt_if_vault_data_encrypted(dataloader):
    with patch('ansible.parsing.dataloader.is_encrypted', return_value=True), \
         patch('ansible.parsing.dataloader.parse_vaulttext_envelope', return_value=(b"ciphertext", b"version", "cipher_name", "vault_id")), \
         patch.object(dataloader, '_vault', create=True) as mock_vault:
        
        mock_vault.decrypt = MagicMock(return_value=b"decrypted data")
        
        b_vault_data = b"encrypted data"
        b_file_name = "dummy_file"
        b_data, show_content = dataloader._decrypt_if_vault_data(b_vault_data, b_file_name)
        
        mock_vault.decrypt.assert_called_once_with(b_vault_data, filename=b_file_name)
        assert b_data == b"decrypted data"
        assert show_content is False
