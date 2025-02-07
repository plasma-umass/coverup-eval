# file: lib/ansible/parsing/dataloader.py:142-169
# asked: {"lines": [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169], "branches": [[155, 156], [155, 158], [161, 162], [161, 164]]}
# gained: {"lines": [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169], "branches": [[155, 156], [155, 158], [161, 162], [161, 164]]}

import pytest
from unittest.mock import mock_open, patch
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
from ansible.module_utils.six import binary_type, text_type
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def dataloader():
    return DataLoader()

def test_get_file_contents_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
        dataloader._get_file_contents(None)
    with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
        dataloader._get_file_contents(123)

@patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='testfile')
@patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=False)
def test_get_file_contents_file_not_found(mock_path_exists, mock_path_dwim, dataloader):
    with pytest.raises(AnsibleFileNotFound, match="Unable to retrieve file contents"):
        dataloader._get_file_contents('testfile')

@patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='testfile')
@patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
@patch('builtins.open', new_callable=mock_open, read_data=b'some data')
@patch('ansible.parsing.dataloader.DataLoader._decrypt_if_vault_data', return_value=b'some data')
def test_get_file_contents_success(mock_decrypt, mock_open, mock_path_exists, mock_path_dwim, dataloader):
    result = dataloader._get_file_contents('testfile')
    assert result == b'some data'
    mock_open.assert_called_once_with(to_bytes('testfile'), 'rb')
    mock_decrypt.assert_called_once_with(b'some data', to_bytes('testfile'))

@patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='testfile')
@patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)
@patch('builtins.open', side_effect=IOError("File error"))
def test_get_file_contents_io_error(mock_open, mock_path_exists, mock_path_dwim, dataloader):
    with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file 'testfile'"):
        dataloader._get_file_contents('testfile')
