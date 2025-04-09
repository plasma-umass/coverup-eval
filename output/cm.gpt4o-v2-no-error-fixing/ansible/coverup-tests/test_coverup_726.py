# file: lib/ansible/parsing/dataloader.py:359-397
# asked: {"lines": [366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [376, 394], [381, 385], [381, 394], [386, 387], [386, 389]]}
# gained: {"lines": [366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [381, 385], [386, 387], [386, 389]]}

import pytest
from unittest.mock import mock_open, patch, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
from ansible.module_utils.six import binary_type, text_type
from ansible.module_utils._text import to_bytes, to_native
from ansible.parsing.vault import is_encrypted_file

@pytest.fixture
def dataloader():
    dl = DataLoader()
    dl._vault = MagicMock()
    dl._vault.secrets = ['secret']
    dl._tempfiles = set()
    return dl

def test_get_real_file_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
        dataloader.get_real_file(None)

    with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
        dataloader.get_real_file(123)

def test_get_real_file_file_not_found(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: False)
    with pytest.raises(AnsibleFileNotFound, match="Could not find or access 'test.txt'"):
        dataloader.get_real_file('test.txt')

    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: False)
    with pytest.raises(AnsibleFileNotFound, match="Could not find or access 'test.txt'"):
        dataloader.get_real_file('test.txt')

def test_get_real_file_encrypted_file_no_secret(dataloader, monkeypatch):
    dataloader._vault.secrets = []
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    mock_file = mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')
    monkeypatch.setattr('builtins.open', mock_file)
    monkeypatch.setattr('ansible.parsing.vault.is_encrypted_file', lambda x, count: True)

    with pytest.raises(AnsibleParserError, match="A vault password or secret must be specified to decrypt test.txt"):
        dataloader.get_real_file('test.txt')

def test_get_real_file_encrypted_file_with_secret(dataloader, monkeypatch):
    dataloader._vault.decrypt = lambda data, filename: b'decrypted content'
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    mock_file = mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')
    monkeypatch.setattr('builtins.open', mock_file)
    monkeypatch.setattr('ansible.parsing.vault.is_encrypted_file', lambda x, count: True)
    monkeypatch.setattr(dataloader, '_create_content_tempfile', lambda x: 'tempfile_path')

    result = dataloader.get_real_file('test.txt')
    assert result == 'tempfile_path'
    assert 'tempfile_path' in dataloader._tempfiles

def test_get_real_file_io_error(dataloader, monkeypatch):
    monkeypatch.setattr(dataloader, 'path_exists', lambda x: True)
    monkeypatch.setattr(dataloader, 'is_file', lambda x: True)
    monkeypatch.setattr(dataloader, 'path_dwim', lambda x: x)
    mock_file = mock_open()
    mock_file.side_effect = IOError("IO error")
    monkeypatch.setattr('builtins.open', mock_file)

    with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file 'test.txt': IO error"):
        dataloader.get_real_file('test.txt')
