# file: lib/ansible/parsing/dataloader.py:197-229
# asked: {"lines": [197, 200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}
# gained: {"lines": [197, 200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}

import os
import pytest
from unittest.mock import patch, mock_open
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_role_with_tasks_in_path(dataloader):
    path = 'some/role/tasks'
    with patch('os.path.exists', return_value=True):
        assert dataloader._is_role(path) is True

def test_is_role_with_main_yml(dataloader):
    path = 'some/role'
    with patch('os.path.exists', side_effect=lambda p: p.endswith(b'main.yml')):
        assert dataloader._is_role(path) is True

def test_is_role_with_main_yaml(dataloader):
    path = 'some/role'
    with patch('os.path.exists', side_effect=lambda p: p.endswith(b'main.yaml')):
        assert dataloader._is_role(path) is True

def test_is_role_with_main(dataloader):
    path = 'some/role'
    with patch('os.path.exists', side_effect=lambda p: p.endswith(b'main')):
        assert dataloader._is_role(path) is True

def test_is_role_without_tasks_or_main(dataloader):
    path = 'some/role'
    with patch('os.path.exists', return_value=False):
        assert dataloader._is_role(path) is False
