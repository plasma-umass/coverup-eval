# file: lib/ansible/parsing/dataloader.py:197-229
# asked: {"lines": [197, 200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}
# gained: {"lines": [197, 200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_role_with_tasks_main_yml(dataloader, monkeypatch):
    path = 'roles/myrole/tasks/main.yml'
    
    def mock_exists(path):
        return path.endswith(b'tasks/main.yml')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_meta_main_yml(dataloader, monkeypatch):
    path = 'roles/myrole/meta/main.yml'
    
    def mock_exists(path):
        return path.endswith(b'meta/main.yml')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_main_yml(dataloader, monkeypatch):
    path = 'roles/myrole/main.yml'
    
    def mock_exists(path):
        return path.endswith(b'main.yml')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_no_main_files(dataloader, monkeypatch):
    path = 'roles/myrole/README.md'
    
    def mock_exists(path):
        return False
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == False

def test_is_role_with_tasks_main_yaml(dataloader, monkeypatch):
    path = 'roles/myrole/tasks/main.yaml'
    
    def mock_exists(path):
        return path.endswith(b'tasks/main.yaml')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_meta_main_yaml(dataloader, monkeypatch):
    path = 'roles/myrole/meta/main.yaml'
    
    def mock_exists(path):
        return path.endswith(b'meta/main.yaml')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_main_yaml(dataloader, monkeypatch):
    path = 'roles/myrole/main.yaml'
    
    def mock_exists(path):
        return path.endswith(b'main.yaml')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_tasks_main(dataloader, monkeypatch):
    path = 'roles/myrole/tasks/main'
    
    def mock_exists(path):
        return path.endswith(b'tasks/main')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_meta_main(dataloader, monkeypatch):
    path = 'roles/myrole/meta/main'
    
    def mock_exists(path):
        return path.endswith(b'meta/main')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True

def test_is_role_with_main(dataloader, monkeypatch):
    path = 'roles/myrole/main'
    
    def mock_exists(path):
        return path.endswith(b'main')
    
    monkeypatch.setattr(os.path, 'exists', mock_exists)
    
    assert dataloader._is_role(path) == True
