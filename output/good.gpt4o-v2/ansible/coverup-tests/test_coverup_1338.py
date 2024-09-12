# file: lib/ansible/parsing/dataloader.py:231-284
# asked: {"lines": [240, 241, 244, 245, 248, 249, 252, 253, 255, 256, 258, 259, 261, 262, 264, 266, 269, 272, 275, 278, 280, 281, 282, 284], "branches": [[244, 245], [244, 248], [252, 253], [252, 255], [255, 256], [255, 258], [264, 266], [264, 269], [280, 281], [280, 284], [281, 280], [281, 282]]}
# gained: {"lines": [240, 241, 244, 245, 248, 249, 252, 253, 255, 258, 259, 261, 262, 264, 266, 269, 272, 275, 278, 280, 281, 282, 284], "branches": [[244, 245], [244, 248], [252, 253], [255, 258], [264, 266], [280, 281], [281, 282]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible.utils.path import unfrackpath

@pytest.fixture
def dataloader():
    return DataLoader()

@pytest.fixture
def mock_is_role():
    with patch('ansible.parsing.dataloader.DataLoader._is_role', return_value=True) as mock:
        yield mock

@pytest.fixture
def mock_set_basedir():
    with patch('ansible.parsing.dataloader.DataLoader.set_basedir') as mock:
        yield mock

@pytest.fixture
def mock_path_dwim():
    with patch('ansible.parsing.dataloader.DataLoader.path_dwim', side_effect=lambda x: x) as mock:
        yield mock

@pytest.fixture
def mock_os_path_exists():
    with patch('os.path.exists', return_value=True) as mock:
        yield mock

def test_path_dwim_relative_full_coverage(dataloader, mock_is_role, mock_set_basedir, mock_path_dwim, mock_os_path_exists):
    path = '/some/path'
    dirname = 'templates'
    source = 'file.txt'
    
    result = dataloader.path_dwim_relative(path, dirname, source, is_role=False)
    
    assert result == os.path.join(path, dirname, source)
    mock_is_role.assert_called_once_with(path)
    mock_set_basedir.assert_called()
    mock_path_dwim.assert_any_call(os.path.join(dirname, source))
    mock_path_dwim.assert_any_call(source)
    mock_os_path_exists.assert_called()

def test_path_dwim_relative_with_absolute_source(dataloader, mock_os_path_exists):
    path = '/some/path'
    dirname = 'templates'
    source = '/absolute/path/to/file.txt'
    
    result = dataloader.path_dwim_relative(path, dirname, source, is_role=False)
    
    assert result == unfrackpath(source, follow=False)
    mock_os_path_exists.assert_called()

def test_path_dwim_relative_with_tilde_source(dataloader, mock_os_path_exists):
    path = '/some/path'
    dirname = 'templates'
    source = '~/file.txt'
    
    result = dataloader.path_dwim_relative(path, dirname, source, is_role=False)
    
    assert result == unfrackpath(source, follow=False)
    mock_os_path_exists.assert_called()
