# file: lib/ansible/parsing/dataloader.py:197-229
# asked: {"lines": [197, 200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}
# gained: {"lines": [197, 200, 201, 202, 204, 205, 206, 207, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 224, 225, 226, 227, 229], "branches": [[226, 227], [226, 229]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

@pytest.fixture
def mock_os_path_exists():
    with patch('os.path.exists') as mock_exists:
        yield mock_exists

@pytest.fixture
def mock_to_bytes():
    with patch('ansible.module_utils._text.to_bytes', side_effect=lambda x, errors='strict': x.encode('utf-8')):
        yield

@pytest.fixture
def mock_unfrackpath():
    with patch('ansible.utils.path.unfrackpath', side_effect=lambda x, follow=False: x):
        yield

@pytest.fixture
def mock_re_tasks():
    with patch('ansible.parsing.dataloader.RE_TASKS') as mock_re:
        mock_re.search = MagicMock(return_value=True)
        yield mock_re

def test_is_role_with_tasked_paths(dataloader, mock_os_path_exists, mock_to_bytes, mock_unfrackpath, mock_re_tasks):
    mock_os_path_exists.side_effect = lambda x: x.endswith(b'tasks/main.yml')
    path = 'some/role/path'
    assert dataloader._is_role(path) == True

def test_is_role_with_untasked_paths(dataloader, mock_os_path_exists, mock_to_bytes, mock_unfrackpath, mock_re_tasks):
    mock_os_path_exists.side_effect = lambda x: x.endswith(b'main.yml')
    path = 'some/role/path'
    assert dataloader._is_role(path) == True

def test_is_role_with_no_matching_paths(dataloader, mock_os_path_exists, mock_to_bytes, mock_unfrackpath, mock_re_tasks):
    mock_os_path_exists.return_value = False
    path = 'some/role/path'
    assert dataloader._is_role(path) == False
