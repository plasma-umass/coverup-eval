# file lib/ansible/parsing/dataloader.py:359-397
# lines []
# branches ['376->394']

import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleParserError, AnsibleFileNotFound

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._vault = mock.Mock()
    loader._vault.secrets = ['secret']
    loader._vault.decrypt = mock.Mock(return_value=b'decrypted content')
    loader._create_content_tempfile = mock.Mock(return_value='/tmp/decrypted_file')
    loader._tempfiles = set()
    return loader

@pytest.fixture
def mock_open(mocker):
    return mocker.patch('builtins.open', mock.mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n'))

@pytest.fixture
def mock_is_encrypted_file(mocker):
    return mocker.patch('ansible.parsing.vault.is_encrypted_file', return_value=True)

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.parsing.dataloader.to_bytes', side_effect=lambda x, **kwargs: x.encode() if isinstance(x, str) else x)

@pytest.fixture
def mock_to_native(mocker):
    return mocker.patch('ansible.parsing.dataloader.to_native', side_effect=lambda x: x.decode() if isinstance(x, bytes) else x)

@pytest.fixture
def mock_path_exists(mocker):
    return mocker.patch('ansible.parsing.dataloader.DataLoader.path_exists', return_value=True)

@pytest.fixture
def mock_is_file(mocker):
    return mocker.patch('ansible.parsing.dataloader.DataLoader.is_file', return_value=True)

@pytest.fixture
def mock_path_dwim(mocker):
    return mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', side_effect=lambda x: x)

def test_get_real_file_decrypt(dataloader, mock_open, mock_is_encrypted_file, mock_to_bytes, mock_to_native, mock_path_exists, mock_is_file, mock_path_dwim):
    file_path = 'testfile'
    result = dataloader.get_real_file(file_path, decrypt=True)
    
    # Assertions to verify the correct behavior
    assert result == '/tmp/decrypted_file'
    dataloader._vault.decrypt.assert_called_once()
    dataloader._create_content_tempfile.assert_called_once()
    assert '/tmp/decrypted_file' in dataloader._tempfiles

def test_get_real_file_no_decrypt(dataloader, mock_open, mock_is_encrypted_file, mock_to_bytes, mock_to_native, mock_path_exists, mock_is_file, mock_path_dwim):
    file_path = 'testfile'
    result = dataloader.get_real_file(file_path, decrypt=False)
    
    # Assertions to verify the correct behavior
    assert result == file_path
    dataloader._vault.decrypt.assert_not_called()
    dataloader._create_content_tempfile.assert_not_called()
    assert '/tmp/decrypted_file' not in dataloader._tempfiles
