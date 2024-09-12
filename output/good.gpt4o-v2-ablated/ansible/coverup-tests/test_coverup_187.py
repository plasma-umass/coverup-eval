# file: lib/ansible/parsing/dataloader.py:129-140
# asked: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}
# gained: {"lines": [129, 132, 133, 134, 136, 137, 139, 140], "branches": [[132, 133], [132, 136]]}

import pytest
from unittest.mock import Mock, patch

# Assuming the DataLoader class and its dependencies are in a module named dataloader
from ansible.parsing.dataloader import DataLoader

# Mocking the dependencies
def is_encrypted(data):
    return data.startswith(b'$ANSIBLE_VAULT;')

def parse_vaulttext_envelope(data):
    return b'ciphertext', b'1.1', 'AES256', 'vault_id'

class MockVault:
    def decrypt(self, data, filename=None):
        return b'decrypted_data'

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._vault = MockVault()
    return loader

def test_decrypt_if_vault_data_not_encrypted(dataloader, monkeypatch):
    monkeypatch.setattr('ansible.parsing.dataloader.is_encrypted', lambda x: False)
    b_vault_data = b'plain_data'
    b_file_name = 'testfile'
    
    result, show_content = dataloader._decrypt_if_vault_data(b_vault_data, b_file_name)
    
    assert result == b_vault_data
    assert show_content is True

def test_decrypt_if_vault_data_encrypted(dataloader, monkeypatch):
    monkeypatch.setattr('ansible.parsing.dataloader.is_encrypted', lambda x: True)
    monkeypatch.setattr('ansible.parsing.dataloader.parse_vaulttext_envelope', parse_vaulttext_envelope)
    
    b_vault_data = b'$ANSIBLE_VAULT;1.1;AES256'
    b_file_name = 'testfile'
    
    result, show_content = dataloader._decrypt_if_vault_data(b_vault_data, b_file_name)
    
    assert result == b'decrypted_data'
    assert show_content is False
