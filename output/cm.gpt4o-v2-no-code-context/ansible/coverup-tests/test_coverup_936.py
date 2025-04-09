# file: lib/ansible/parsing/dataloader.py:420-452
# asked: {"lines": [427, 428, 430, 432, 434, 436, 437, 438, 439, 441, 443, 444, 445, 446, 448, 450, 451, 452], "branches": [[430, 432], [430, 434], [434, 436], [434, 452], [436, 437], [436, 438], [438, 439], [438, 441], [443, 434], [443, 444], [444, 445], [444, 450], [445, 446], [445, 448]]}
# gained: {"lines": [427, 428, 430, 432, 434, 436, 437, 438, 441, 443, 444, 445, 446, 448, 450, 451, 452], "branches": [[430, 432], [430, 434], [434, 436], [434, 452], [436, 437], [436, 438], [438, 441], [443, 434], [443, 444], [444, 445], [444, 450], [445, 446], [445, 448]]}

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes, to_text
import ansible.constants as C

@pytest.fixture
def dataloader():
    return DataLoader()

def test_find_vars_files_no_extensions(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    b_path = to_bytes(os.path.join(path, name))
    
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=False)
    
    result = dataloader.find_vars_files(path, name)
    
    assert result == [b_path]

def test_find_vars_files_with_extensions(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = ['.yml', '.yaml']
    b_path = to_bytes(os.path.join(path, name))
    
    def path_exists_side_effect(path):
        return path in [b_path + to_bytes(ext) for ext in extensions]
    
    mocker.patch.object(dataloader, 'path_exists', side_effect=path_exists_side_effect)
    mocker.patch.object(dataloader, 'is_directory', return_value=False)
    
    result = dataloader.find_vars_files(path, name, extensions)
    
    expected = [b_path + to_bytes(ext) for ext in extensions]
    assert result == expected[:1]  # Only the first valid extension should be returned

def test_find_vars_files_directory_allowed(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = ['.yml', '.yaml']
    b_path = to_bytes(os.path.join(path, name))
    
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=True)
    mocker.patch.object(dataloader, '_get_dir_vars_files', return_value=[to_text(b_path)])
    
    result = dataloader.find_vars_files(path, name, extensions, allow_dir=True)
    
    assert result == [to_text(b_path)]

def test_find_vars_files_directory_not_allowed(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = ['.yml', '.yaml']
    b_path = to_bytes(os.path.join(path, name))
    
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=True)
    
    result = dataloader.find_vars_files(path, name, extensions, allow_dir=False)
    
    assert result == []

def test_find_vars_files_no_path_exists(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = ['.yml', '.yaml']
    b_path = to_bytes(os.path.join(path, name))
    
    mocker.patch.object(dataloader, 'path_exists', return_value=False)
    
    result = dataloader.find_vars_files(path, name, extensions)
    
    assert result == []
