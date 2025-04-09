# file: lib/ansible/parsing/dataloader.py:359-397
# asked: {"lines": [], "branches": [[376, 394]]}
# gained: {"lines": [], "branches": [[376, 394]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleParserError, AnsibleFileNotFound

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._vault = MagicMock()
    loader._vault.secrets = ['secret']
    loader._vault.decrypt = MagicMock(return_value=b'decrypted content')
    loader._create_content_tempfile = MagicMock(return_value='/tmp/decrypted_file')
    loader._tempfiles = set()
    return loader

def test_get_real_file_not_decrypt(dataloader):
    file_path = 'testfile.txt'
    
    with patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.is_file', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_path):
        
        result = dataloader.get_real_file(file_path, decrypt=False)
        assert result == file_path

def test_get_real_file_decrypt(dataloader):
    file_path = 'testfile.txt'
    encrypted_content = b'$ANSIBLE_VAULT;1.1;AES256\n'
    
    with patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.is_file', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_path), \
         patch('builtins.open', mock_open(read_data=encrypted_content)), \
         patch('ansible.parsing.dataloader.is_encrypted_file', return_value=True):
        
        result = dataloader.get_real_file(file_path, decrypt=True)
        assert result == '/tmp/decrypted_file'
        assert '/tmp/decrypted_file' in dataloader._tempfiles

def test_get_real_file_no_vault_secret(dataloader):
    file_path = 'testfile.txt'
    encrypted_content = b'$ANSIBLE_VAULT;1.1;AES256\n'
    dataloader._vault.secrets = []

    with patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.is_file', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_path), \
         patch('builtins.open', mock_open(read_data=encrypted_content)), \
         patch('ansible.parsing.dataloader.is_encrypted_file', return_value=True):
        
        with pytest.raises(AnsibleParserError, match="A vault password or secret must be specified to decrypt"):
            dataloader.get_real_file(file_path, decrypt=True)

def test_get_real_file_io_error(dataloader):
    file_path = 'testfile.txt'
    
    with patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.is_file', return_value=True), \
         patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value=file_path), \
         patch('builtins.open', side_effect=IOError("Unable to open file")):
        
        with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file"):
            dataloader.get_real_file(file_path, decrypt=True)
