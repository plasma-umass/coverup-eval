# file: lib/ansible/parsing/dataloader.py:359-397
# asked: {"lines": [359, 366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [376, 394], [381, 385], [381, 394], [386, 387], [386, 389]]}
# gained: {"lines": [359, 366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [381, 385], [381, 394], [386, 387], [386, 389]]}

import pytest
from unittest.mock import mock_open, patch, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleParserError, AnsibleFileNotFound

@pytest.fixture
def dataloader():
    dl = DataLoader()
    dl._vault = MagicMock()
    dl._vault.secrets = ['secret']
    dl._create_content_tempfile = MagicMock(return_value='/tmp/decrypted_file')
    dl._tempfiles = set()
    return dl

def test_get_real_file_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
        dataloader.get_real_file(None)

    with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
        dataloader.get_real_file(123)

def test_get_real_file_not_exists(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: False)
    with pytest.raises(AnsibleFileNotFound):
        dataloader.get_real_file('non_existent_file')

def test_get_real_file_not_a_file(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: False)
    with pytest.raises(AnsibleFileNotFound):
        dataloader.get_real_file('not_a_file')

def test_get_real_file_encrypted_no_secret(dataloader, monkeypatch):
    dataloader._vault.secrets = []
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    mock_file = mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')
    with patch('builtins.open', mock_file):
        with pytest.raises(AnsibleParserError, match="A vault password or secret must be specified to decrypt"):
            dataloader.get_real_file('encrypted_file')

def test_get_real_file_encrypted_with_secret(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    mock_file = mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')
    with patch('builtins.open', mock_file):
        dataloader._vault.decrypt = MagicMock(return_value=b'decrypted_content')
        result = dataloader.get_real_file('encrypted_file')
        assert result == '/tmp/decrypted_file'
        assert '/tmp/decrypted_file' in dataloader._tempfiles

def test_get_real_file_plaintext(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    mock_file = mock_open(read_data=b'plain text content')
    with patch('builtins.open', mock_file):
        result = dataloader.get_real_file('plaintext_file')
        assert result == 'plaintext_file'

def test_get_real_file_io_error(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    with patch('builtins.open', mock_open()) as mock_file:
        mock_file.side_effect = IOError("IO error")
        with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file"):
            dataloader.get_real_file('io_error_file')
