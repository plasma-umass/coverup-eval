# file: lib/ansible/parsing/dataloader.py:359-397
# asked: {"lines": [359, 366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [376, 394], [381, 385], [381, 394], [386, 387], [386, 389]]}
# gained: {"lines": [359, 366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [381, 385], [381, 394], [386, 387], [386, 389]]}

import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
from ansible.module_utils.six import binary_type, text_type
from ansible.module_utils._text import to_bytes, to_native
from ansible.parsing.vault import b_HEADER, is_encrypted_file
from ansible.parsing.dataloader import DataLoader

class MockVault:
    def __init__(self, secrets=None):
        self.secrets = secrets or []

    def decrypt(self, data, filename=None):
        return data

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader._vault = MockVault()
    loader._tempfiles = set()
    return loader

def test_get_real_file_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
        dataloader.get_real_file(None)

    with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
        dataloader.get_real_file(123)

def test_get_real_file_not_exists(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: False)
    with pytest.raises(AnsibleFileNotFound, match="Could not find or access 'test.txt'"):
        dataloader.get_real_file('test.txt')

def test_get_real_file_not_a_file(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: False)
    with pytest.raises(AnsibleFileNotFound, match="Could not find or access 'test.txt'"):
        dataloader.get_real_file('test.txt')

def test_get_real_file_encrypted_no_secret(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    dataloader._vault.secrets = []

    m = mock_open(read_data=b_HEADER)
    with patch('builtins.open', m):
        with pytest.raises(AnsibleParserError, match="A vault password or secret must be specified to decrypt test.txt"):
            dataloader.get_real_file('test.txt')

def test_get_real_file_encrypted_with_secret(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    dataloader._vault.secrets = ['secret']

    m = mock_open(read_data=b_HEADER)
    with patch('builtins.open', m):
        with patch.object(dataloader._vault, 'decrypt', return_value=b'decrypted data'):
            with patch.object(dataloader, '_create_content_tempfile', return_value='/tmp/decrypted_file'):
                real_path = dataloader.get_real_file('test.txt')
                assert real_path == '/tmp/decrypted_file'
                assert real_path in dataloader._tempfiles

def test_get_real_file_not_encrypted(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)

    m = mock_open(read_data=b'not encrypted data')
    with patch('builtins.open', m):
        real_path = dataloader.get_real_file('test.txt')
        assert real_path == 'test.txt'

def test_get_real_file_io_error(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)

    m = mock_open()
    m.side_effect = IOError("IO error")
    with patch('builtins.open', m):
        with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file 'test.txt': IO error"):
            dataloader.get_real_file('test.txt')
