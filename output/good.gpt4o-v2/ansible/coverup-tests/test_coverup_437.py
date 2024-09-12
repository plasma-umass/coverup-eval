# file: lib/ansible/parsing/dataloader.py:129-140
# asked: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}
# gained: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}

import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.vault import is_encrypted, parse_vaulttext_envelope
from unittest.mock import patch, MagicMock

@pytest.fixture
def dataloader():
    dl = DataLoader()
    dl._vault = MagicMock()
    return dl

def test_decrypt_if_vault_data_not_encrypted(dataloader):
    data = b"not encrypted data"
    
    with patch('ansible.parsing.vault.is_encrypted', return_value=False):
        result, show_content = dataloader._decrypt_if_vault_data(data)
    
    assert result == data
    assert show_content is True

def test_decrypt_if_vault_data_encrypted(dataloader):
    data = b"$ANSIBLE_VAULT;1.1;AES256\nencrypted data"
    decrypted_data = b"decrypted data"
    
    with patch('ansible.parsing.vault.is_encrypted', return_value=True), \
         patch('ansible.parsing.vault.parse_vaulttext_envelope', return_value=(b"ciphertext", b"1.1", "AES256", "vault_id")), \
         patch.object(dataloader._vault, 'decrypt', return_value=decrypted_data):
        
        result, show_content = dataloader._decrypt_if_vault_data(data)
    
    assert result == decrypted_data
    assert show_content is False
