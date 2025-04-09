# file lib/ansible/parsing/dataloader.py:112-114
# lines [112, 113, 114]
# branches []

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

# Assuming the DataLoader class is part of a larger file, we only need to test the is_file method.

@pytest.fixture
def data_loader():
    return DataLoader()

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "tempfile.txt"
    file.write_text("This is a temporary file.")
    return str(file)

def test_is_file_with_existing_file(data_loader, temp_file):
    assert data_loader.is_file(temp_file) == True

def test_is_file_with_non_existing_file(data_loader):
    assert data_loader.is_file("/non/existing/file.txt") == False

def test_is_file_with_dev_null(data_loader, mocker):
    mocker.patch('os.path.isfile', return_value=False)
    assert data_loader.is_file(os.devnull) == True

# Clean up is handled by pytest's tmp_path fixture, which provides a temporary directory that is unique to the test invocation,
# created in the base temporary directory, and by default, any files created will be deleted after the test session is finished.
