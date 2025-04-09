# file lib/ansible/parsing/dataloader.py:142-169
# lines [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169]
# branches ['155->156', '155->158', '161->162', '161->164']

import pytest
from unittest import mock
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

def test_get_file_contents_file_not_found(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_dwim', return_value='non_existent_file')
    mocker.patch.object(dataloader, 'path_exists', return_value=False)
    
    with pytest.raises(AnsibleFileNotFound, match="Unable to retrieve file contents"):
        dataloader._get_file_contents('non_existent_file')

def test_get_file_contents_io_error(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_dwim', return_value='some_file')
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mock_open = mock.mock_open()
    mock_open.side_effect = IOError("IO error")
    mocker.patch('builtins.open', mock_open)
    
    with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file 'some_file'"):
        dataloader._get_file_contents('some_file')

def test_get_file_contents_success(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_dwim', return_value='some_file')
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mock_open = mock.mock_open(read_data=b'some data')
    mocker.patch('builtins.open', mock_open)
    mocker.patch.object(dataloader, '_decrypt_if_vault_data', return_value=b'some data')
    
    result = dataloader._get_file_contents('some_file')
    assert result == b'some data'
