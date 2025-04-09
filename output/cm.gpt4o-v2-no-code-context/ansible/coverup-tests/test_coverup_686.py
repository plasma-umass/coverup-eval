# file: lib/ansible/parsing/dataloader.py:108-110
# asked: {"lines": [108, 109, 110], "branches": []}
# gained: {"lines": [108, 109, 110], "branches": []}

import os
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_exists_with_existing_path(dataloader, monkeypatch):
    test_path = "/existing/path"
    
    def mock_path_dwim(path):
        return path
    
    def mock_to_bytes(path, errors):
        return path
    
    monkeypatch.setattr(dataloader, 'path_dwim', mock_path_dwim)
    monkeypatch.setattr('ansible.parsing.dataloader.to_bytes', mock_to_bytes)
    monkeypatch.setattr(os.path, 'exists', lambda path: True)
    
    assert dataloader.path_exists(test_path) is True

def test_path_exists_with_non_existing_path(dataloader, monkeypatch):
    test_path = "/non/existing/path"
    
    def mock_path_dwim(path):
        return path
    
    def mock_to_bytes(path, errors):
        return path
    
    monkeypatch.setattr(dataloader, 'path_dwim', mock_path_dwim)
    monkeypatch.setattr('ansible.parsing.dataloader.to_bytes', mock_to_bytes)
    monkeypatch.setattr(os.path, 'exists', lambda path: False)
    
    assert dataloader.path_exists(test_path) is False
