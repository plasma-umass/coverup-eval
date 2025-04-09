# file: lib/ansible/parsing/dataloader.py:231-284
# asked: {"lines": [240, 241, 244, 245, 248, 249, 252, 253, 255, 256, 258, 259, 261, 262, 264, 266, 269, 272, 275, 278, 280, 281, 282, 284], "branches": [[244, 245], [244, 248], [252, 253], [252, 255], [255, 256], [255, 258], [264, 266], [264, 269], [280, 281], [280, 284], [281, 280], [281, 282]]}
# gained: {"lines": [240, 241, 244, 245, 248, 249, 252, 253, 255, 256, 258, 259, 261, 262, 264, 266, 269, 272, 275, 278, 280, 281, 282, 284], "branches": [[244, 245], [244, 248], [252, 253], [255, 256], [255, 258], [264, 266], [264, 269], [280, 281], [281, 282]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes, to_text
from ansible.utils.path import unfrackpath

@pytest.fixture
def dataloader():
    return DataLoader()

@pytest.fixture
def mock_is_role():
    with patch.object(DataLoader, '_is_role', return_value=False) as mock:
        yield mock

@pytest.fixture
def mock_set_basedir():
    with patch.object(DataLoader, 'set_basedir') as mock:
        yield mock

@pytest.fixture
def mock_path_dwim():
    with patch.object(DataLoader, 'path_dwim', side_effect=lambda x: x) as mock:
        yield mock

@pytest.fixture
def mock_os_path_exists():
    with patch('os.path.exists', return_value=True) as mock:
        yield mock

def test_path_dwim_relative_absolute_path(dataloader, mock_set_basedir, mock_path_dwim, mock_os_path_exists):
    path = "/absolute/path"
    dirname = "templates"
    source = "/absolute/source/file"
    
    result = dataloader.path_dwim_relative(path, dirname, source)
    
    assert result == unfrackpath(source, follow=False)
    mock_set_basedir.assert_not_called()
    mock_path_dwim.assert_not_called()

def test_path_dwim_relative_relative_path(dataloader, mock_is_role, mock_set_basedir, mock_path_dwim, mock_os_path_exists):
    path = "/relative/path"
    dirname = "templates"
    source = "relative/source/file"
    
    result = dataloader.path_dwim_relative(path, dirname, source)
    
    expected_search = [
        os.path.join(path, dirname, source),
        unfrackpath(os.path.join(path, dirname, source), follow=False),
        unfrackpath(os.path.join(dirname, source), follow=False),
        unfrackpath(os.path.join(path, source), follow=False),
        os.path.join(dirname, source),
        source
    ]
    
    assert result in expected_search
    mock_set_basedir.assert_called()
    mock_path_dwim.assert_called()

def test_path_dwim_relative_role_path(dataloader, mock_set_basedir, mock_path_dwim, mock_os_path_exists):
    path = "/role/path/tasks"
    dirname = "templates"
    source = "relative/source/file"
    
    with patch.object(DataLoader, '_is_role', return_value=True):
        result = dataloader.path_dwim_relative(path, dirname, source)
    
    expected_search = [
        os.path.join(path, dirname, source),
        unfrackpath(os.path.join(os.path.dirname(path), dirname, source), follow=False),
        unfrackpath(os.path.join(os.path.dirname(path), 'tasks', source), follow=False),
        unfrackpath(os.path.join(dirname, source), follow=False),
        unfrackpath(os.path.join(os.path.dirname(path), source), follow=False),
        os.path.join(dirname, source),
        source
    ]
    
    assert result in expected_search
    mock_set_basedir.assert_called()
    mock_path_dwim.assert_called()
