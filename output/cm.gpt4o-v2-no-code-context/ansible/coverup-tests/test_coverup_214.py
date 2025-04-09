# file: lib/ansible/parsing/dataloader.py:142-169
# asked: {"lines": [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169], "branches": [[155, 156], [155, 158], [161, 162], [161, 164]]}
# gained: {"lines": [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169], "branches": [[155, 156], [155, 158], [161, 162], [161, 164]]}

import pytest
from unittest.mock import mock_open, patch, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def dataloader():
    return DataLoader()

def test_get_file_contents_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
        dataloader._get_file_contents(None)

    with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
        dataloader._get_file_contents(123)

def test_get_file_contents_file_not_found(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: False)
    
    with pytest.raises(AnsibleFileNotFound, match="Unable to retrieve file contents"):
        dataloader._get_file_contents('non_existent_file.txt')

def test_get_file_contents_io_error(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    
    with patch('builtins.open', mock_open()) as mocked_open:
        mocked_open.side_effect = IOError("Unable to open file")
        
        with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file 'test_file.txt'"):
            dataloader._get_file_contents('test_file.txt')

def test_get_file_contents_success(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    mock_data = b"test data"
    
    with patch('builtins.open', mock_open(read_data=mock_data)) as mocked_open:
        monkeypatch.setattr(dataloader, '_decrypt_if_vault_data', lambda data, filename: data)
        
        result = dataloader._get_file_contents('test_file.txt')
        assert result == mock_data
        mocked_open.assert_called_once_with(to_bytes('test_file.txt'), 'rb')
