# file: lib/ansible/parsing/dataloader.py:120-122
# asked: {"lines": [120, 121, 122], "branches": []}
# gained: {"lines": [120, 121, 122], "branches": []}

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_list_directory(dataloader, monkeypatch):
    test_path = "/test/path"
    dwim_path = "/dwim/path"
    expected_files = ["file1.txt", "file2.txt"]

    def mock_path_dwim(path):
        assert path == test_path
        return dwim_path

    def mock_listdir(path):
        assert path == dwim_path
        return expected_files

    monkeypatch.setattr(dataloader, "path_dwim", mock_path_dwim)
    monkeypatch.setattr(os, "listdir", mock_listdir)

    result = dataloader.list_directory(test_path)
    assert result == expected_files
