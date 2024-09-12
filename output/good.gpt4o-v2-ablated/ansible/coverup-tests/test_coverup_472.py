# file: lib/ansible/parsing/dataloader.py:108-110
# asked: {"lines": [109, 110], "branches": []}
# gained: {"lines": [109, 110], "branches": []}

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_exists_file_exists(dataloader, monkeypatch):
    test_path = "/fake/path/to/file"
    
    def mock_path_dwim(path):
        return path
    
    def mock_to_bytes(path, errors):
        return path
    
    monkeypatch.setattr(dataloader, 'path_dwim', mock_path_dwim)
    monkeypatch.setattr('ansible.parsing.dataloader.to_bytes', mock_to_bytes)
    monkeypatch.setattr(os.path, 'exists', lambda x: True)
    
    assert dataloader.path_exists(test_path) is True

def test_path_exists_file_does_not_exist(dataloader, monkeypatch):
    test_path = "/fake/path/to/nonexistent/file"
    
    def mock_path_dwim(path):
        return path
    
    def mock_to_bytes(path, errors):
        return path
    
    monkeypatch.setattr(dataloader, 'path_dwim', mock_path_dwim)
    monkeypatch.setattr('ansible.parsing.dataloader.to_bytes', mock_to_bytes)
    monkeypatch.setattr(os.path, 'exists', lambda x: False)
    
    assert dataloader.path_exists(test_path) is False
