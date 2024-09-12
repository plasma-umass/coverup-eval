# file: lib/ansible/parsing/dataloader.py:112-114
# asked: {"lines": [112, 113, 114], "branches": []}
# gained: {"lines": [112, 113, 114], "branches": []}

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_file_with_existing_file(dataloader, tmp_path):
    # Create a temporary file
    temp_file = tmp_path / "temp_file.txt"
    temp_file.write_text("content")

    # Mock path_dwim to return the path of the temporary file
    dataloader.path_dwim = lambda x: str(temp_file)

    # Test is_file method
    assert dataloader.is_file(str(temp_file)) is True

def test_is_file_with_non_existing_file(dataloader):
    # Mock path_dwim to return a non-existing path
    dataloader.path_dwim = lambda x: "/non/existing/path"

    # Test is_file method
    assert dataloader.is_file("/non/existing/path") is False

def test_is_file_with_devnull(dataloader):
    # Mock path_dwim to return os.devnull
    dataloader.path_dwim = lambda x: os.devnull

    # Test is_file method
    assert dataloader.is_file(os.devnull) is True
