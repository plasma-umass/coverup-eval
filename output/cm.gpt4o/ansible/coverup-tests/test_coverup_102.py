# file lib/ansible/parsing/dataloader.py:359-397
# lines [359, 366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397]
# branches ['366->367', '366->369', '370->371', '370->373', '376->377', '376->394', '381->385', '381->394', '386->387', '386->389']

import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleParserError, AnsibleFileNotFound
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._vault = mock.Mock()
    loader._vault.secrets = ['secret']
    loader._vault.decrypt = mock.Mock(return_value=b'decrypted content')
    loader._create_content_tempfile = mock.Mock(return_value='/tmp/decrypted_file')
    loader._tempfiles = set()
    return loader

def test_get_real_file_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
        dataloader.get_real_file(None)

    with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
        dataloader.get_real_file(123)

def test_get_real_file_not_exists(dataloader):
    dataloader.path_exists = mock.Mock(return_value=False)
    dataloader.is_file = mock.Mock(return_value=True)
    with pytest.raises(AnsibleFileNotFound):
        dataloader.get_real_file('non_existent_file')

def test_get_real_file_not_a_file(dataloader):
    dataloader.path_exists = mock.Mock(return_value=True)
    dataloader.is_file = mock.Mock(return_value=False)
    with pytest.raises(AnsibleFileNotFound):
        dataloader.get_real_file('not_a_file')

def test_get_real_file_encrypted_no_password(dataloader):
    dataloader.path_exists = mock.Mock(return_value=True)
    dataloader.is_file = mock.Mock(return_value=True)
    dataloader.path_dwim = mock.Mock(return_value='/tmp/encrypted_file')
    dataloader._vault.secrets = []
    
    with mock.patch('builtins.open', mock.mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')):
        with pytest.raises(AnsibleParserError, match="A vault password or secret must be specified to decrypt"):
            dataloader.get_real_file('encrypted_file')

def test_get_real_file_encrypted_with_password(dataloader):
    dataloader.path_exists = mock.Mock(return_value=True)
    dataloader.is_file = mock.Mock(return_value=True)
    dataloader.path_dwim = mock.Mock(return_value='/tmp/encrypted_file')
    
    with mock.patch('builtins.open', mock.mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')):
        real_path = dataloader.get_real_file('encrypted_file')
        assert real_path == '/tmp/decrypted_file'
        assert '/tmp/decrypted_file' in dataloader._tempfiles

def test_get_real_file_plaintext(dataloader):
    dataloader.path_exists = mock.Mock(return_value=True)
    dataloader.is_file = mock.Mock(return_value=True)
    dataloader.path_dwim = mock.Mock(return_value='/tmp/plaintext_file')
    
    with mock.patch('builtins.open', mock.mock_open(read_data=b'plain text content')):
        real_path = dataloader.get_real_file('plaintext_file')
        assert real_path == '/tmp/plaintext_file'
        assert '/tmp/decrypted_file' not in dataloader._tempfiles

def test_get_real_file_io_error(dataloader):
    dataloader.path_exists = mock.Mock(return_value=True)
    dataloader.is_file = mock.Mock(return_value=True)
    dataloader.path_dwim = mock.Mock(return_value='/tmp/file_with_error')
    
    with mock.patch('builtins.open', mock.mock_open()) as mock_file:
        mock_file.side_effect = IOError("IO error")
        with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file"):
            dataloader.get_real_file('file_with_error')
