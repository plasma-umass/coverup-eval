# file: lib/ansible/parsing/dataloader.py:112-114
# asked: {"lines": [112, 113, 114], "branches": []}
# gained: {"lines": [112, 113, 114], "branches": []}

import os
import pytest
from ansible.module_utils._text import to_bytes
from ansible.parsing.dataloader import DataLoader

class MockDataLoader(DataLoader):
    def __init__(self, basedir):
        self._basedir = basedir

@pytest.fixture
def dataloader(tmp_path):
    basedir = tmp_path / "basedir"
    basedir.mkdir()
    return MockDataLoader(basedir)

def test_is_file_with_existing_file(dataloader, tmp_path):
    test_file = tmp_path / "basedir" / "testfile.txt"
    test_file.write_text("content")
    
    assert dataloader.is_file("testfile.txt") is True

def test_is_file_with_non_existing_file(dataloader):
    assert dataloader.is_file("nonexistentfile.txt") is False

def test_is_file_with_devnull(dataloader):
    assert dataloader.is_file(os.devnull) is True

def test_is_file_with_absolute_path(dataloader, tmp_path):
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("content")
    
    assert dataloader.is_file(str(test_file)) is True

def test_is_file_with_relative_path(dataloader, tmp_path):
    test_file = tmp_path / "basedir" / "testfile.txt"
    test_file.write_text("content")
    
    assert dataloader.is_file("testfile.txt") is True
