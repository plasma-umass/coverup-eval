# file lib/ansible/parsing/dataloader.py:116-118
# lines [116, 117, 118]
# branches []

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

# Assuming the DataLoader class is part of a larger file, we only need to test the is_directory method.

@pytest.fixture
def data_loader():
    return DataLoader()

@pytest.fixture
def temp_dir(tmp_path):
    d = tmp_path / "subdirectory"
    d.mkdir()
    return str(d)

@pytest.fixture
def temp_file(tmp_path):
    f = tmp_path / "file.txt"
    f.touch()
    return str(f)

def test_is_directory_with_directory(data_loader, temp_dir):
    assert data_loader.is_directory(temp_dir) == True

def test_is_directory_with_file(data_loader, temp_file):
    assert data_loader.is_directory(temp_file) == False

def test_is_directory_with_nonexistent_path(data_loader):
    assert data_loader.is_directory('/nonexistent/path') == False
