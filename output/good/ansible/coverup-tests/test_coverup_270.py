# file lib/ansible/parsing/dataloader.py:142-169
# lines [142, 155, 156, 158, 161, 162, 164, 165, 166, 167, 168, 169]
# branches ['155->156', '155->158', '161->162', '161->164']

import os
import pytest
from ansible.errors import AnsibleFileNotFound, AnsibleParserError
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes, to_native
from ansible.module_utils.six import binary_type, text_type

# Assuming the DataLoader class is part of a module named `ansible.parsing.dataloader`
# and the necessary imports are available in the test environment.

@pytest.fixture
def dataloader(mocker):
    # Mocking the _decrypt_if_vault_data method to return the data as is
    mocker.patch.object(DataLoader, '_decrypt_if_vault_data', side_effect=lambda data, filename: data)
    return DataLoader()

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test_file.txt"
    file.write_text(u"Test content")
    return str(file)

def test_get_file_contents_invalid_filename(dataloader):
    with pytest.raises(AnsibleParserError):
        dataloader._get_file_contents(None)

def test_get_file_contents_file_not_found(dataloader):
    with pytest.raises(AnsibleFileNotFound):
        dataloader._get_file_contents("non_existent_file.txt")

def test_get_file_contents_io_error(mocker, dataloader, temp_file):
    mocker.patch('builtins.open', side_effect=IOError("Test IO error"))
    with pytest.raises(AnsibleParserError):
        dataloader._get_file_contents(temp_file)

def test_get_file_contents_os_error(mocker, dataloader, temp_file):
    mocker.patch('builtins.open', side_effect=OSError("Test OS error"))
    with pytest.raises(AnsibleParserError):
        dataloader._get_file_contents(temp_file)

def test_get_file_contents_success(dataloader, temp_file):
    content = dataloader._get_file_contents(temp_file)
    assert content == b"Test content"

# Cleanup is handled by pytest's tmp_path fixture, which provides a temporary directory
# that is unique to the test function and is deleted after the test finishes.
