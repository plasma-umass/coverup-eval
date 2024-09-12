# file: lib/ansible/parsing/dataloader.py:359-397
# asked: {"lines": [359, 366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [376, 394], [381, 385], [381, 394], [386, 387], [386, 389]]}
# gained: {"lines": [359, 366, 367, 369, 370, 371, 373, 375, 376, 377, 381, 385, 386, 387, 389, 391, 392, 394, 396, 397], "branches": [[366, 367], [366, 369], [370, 371], [370, 373], [376, 377], [381, 385], [381, 394], [386, 387], [386, 389]]}

import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.errors import AnsibleParserError, AnsibleFileNotFound
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes, to_native

@pytest.fixture
def dataloader():
    loader = DataLoader()
    loader.path_exists = MagicMock()
    loader.is_file = MagicMock()
    loader.path_dwim = MagicMock()
    loader._vault = MagicMock()
    loader._create_content_tempfile = MagicMock()
    loader._tempfiles = set()
    return loader

def test_get_real_file_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError, match="Invalid filename: 'None'"):
        dataloader.get_real_file(None)

    with pytest.raises(AnsibleParserError, match="Invalid filename: '123'"):
        dataloader.get_real_file(123)

def test_get_real_file_not_exists(dataloader):
    dataloader.path_exists.return_value = False
    with pytest.raises(AnsibleFileNotFound):
        dataloader.get_real_file("nonexistent_file")

def test_get_real_file_not_a_file(dataloader):
    dataloader.path_exists.return_value = True
    dataloader.is_file.return_value = False
    with pytest.raises(AnsibleFileNotFound):
        dataloader.get_real_file("not_a_file")

def test_get_real_file_encrypted_no_password(dataloader):
    dataloader.path_exists.return_value = True
    dataloader.is_file.return_value = True
    dataloader.path_dwim.return_value = "encrypted_file"
    dataloader._vault.secrets = []

    with patch("builtins.open", mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')):
        with pytest.raises(AnsibleParserError, match="A vault password or secret must be specified to decrypt"):
            dataloader.get_real_file("encrypted_file")

def test_get_real_file_encrypted_with_password(dataloader):
    dataloader.path_exists.return_value = True
    dataloader.is_file.return_value = True
    dataloader.path_dwim.return_value = "encrypted_file"
    dataloader._vault.secrets = ["secret"]
    dataloader._vault.decrypt.return_value = b"decrypted content"
    dataloader._create_content_tempfile.return_value = "temp_file"

    with patch("builtins.open", mock_open(read_data=b'$ANSIBLE_VAULT;1.1;AES256\n')):
        result = dataloader.get_real_file("encrypted_file")
        assert result == "temp_file"
        assert "temp_file" in dataloader._tempfiles

def test_get_real_file_not_encrypted(dataloader):
    dataloader.path_exists.return_value = True
    dataloader.is_file.return_value = True
    dataloader.path_dwim.return_value = "plain_file"

    with patch("builtins.open", mock_open(read_data=b'plain content')):
        result = dataloader.get_real_file("plain_file")
        assert result == "plain_file"

def test_get_real_file_io_error(dataloader):
    dataloader.path_exists.return_value = True
    dataloader.is_file.return_value = True
    dataloader.path_dwim.return_value = "some_file"

    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = IOError("IO error")
        with pytest.raises(AnsibleParserError, match="an error occurred while trying to read the file"):
            dataloader.get_real_file("some_file")
