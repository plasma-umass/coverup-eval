# file: lib/ansible/parsing/dataloader.py:129-140
# asked: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}
# gained: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_decrypt_if_vault_data_not_encrypted(dataloader):
    b_vault_data = b'not encrypted data'
    
    with patch('ansible.parsing.dataloader.is_encrypted', return_value=False):
        result, show_content = dataloader._decrypt_if_vault_data(b_vault_data)
    
    assert result == b_vault_data
    assert show_content is True

def test_decrypt_if_vault_data_encrypted(dataloader):
    b_vault_data = b'$ANSIBLE_VAULT;1.1;AES256'
    b_decrypted_data = b'decrypted data'
    b_file_name = 'test_file.yml'
    
    with patch('ansible.parsing.dataloader.is_encrypted', return_value=True), \
         patch('ansible.parsing.dataloader.parse_vaulttext_envelope', return_value=(b'ciphertext', b'1.1', 'AES256', 'vault_id')), \
         patch.object(dataloader._vault, 'decrypt', return_value=b_decrypted_data):
        
        result, show_content = dataloader._decrypt_if_vault_data(b_vault_data, b_file_name)
    
    assert result == b_decrypted_data
    assert show_content is False
