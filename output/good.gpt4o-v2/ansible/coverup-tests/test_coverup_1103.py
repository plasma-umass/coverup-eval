# file: lib/ansible/parsing/dataloader.py:420-452
# asked: {"lines": [427, 428, 430, 432, 434, 436, 437, 438, 439, 441, 443, 444, 445, 446, 448, 450, 451, 452], "branches": [[430, 432], [430, 434], [434, 436], [434, 452], [436, 437], [436, 438], [438, 439], [438, 441], [443, 434], [443, 444], [444, 445], [444, 450], [445, 446], [445, 448]]}
# gained: {"lines": [427, 428, 430, 432, 434, 436, 437, 438, 441, 443, 444, 445, 446, 448, 450, 451, 452], "branches": [[430, 432], [430, 434], [434, 436], [434, 452], [436, 437], [436, 438], [438, 441], [443, 434], [443, 444], [444, 445], [444, 450], [445, 446], [445, 448]]}

import os
import pytest
from unittest.mock import MagicMock
from ansible.parsing.dataloader import DataLoader
from ansible import constants as C
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def dataloader():
    return DataLoader()

def test_find_vars_files_no_extensions(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=False)
    path = '/some/path'
    name = 'vars'
    result = dataloader.find_vars_files(path, name)
    assert result == [to_bytes(os.path.join(path, name))]

def test_find_vars_files_with_extensions(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_exists', side_effect=[True, False])
    mocker.patch.object(dataloader, 'is_directory', return_value=False)
    path = '/some/path'
    name = 'vars'
    extensions = ['.yml', '.yaml']
    result = dataloader.find_vars_files(path, name, extensions)
    expected = [to_bytes(os.path.join(path, name + extensions[0]))]
    assert result == expected

def test_find_vars_files_directory_allowed(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=True)
    mocker.patch.object(dataloader, '_get_dir_vars_files', return_value=[to_bytes('/some/path/vars/file1.yml')])
    path = '/some/path'
    name = 'vars'
    result = dataloader.find_vars_files(path, name)
    assert result == [to_bytes('/some/path/vars/file1.yml')]

def test_find_vars_files_directory_not_allowed(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=True)
    path = '/some/path'
    name = 'vars'
    result = dataloader.find_vars_files(path, name, allow_dir=False)
    assert result == []

def test_find_vars_files_no_path_exists(dataloader, mocker):
    mocker.patch.object(dataloader, 'path_exists', return_value=False)
    path = '/some/path'
    name = 'vars'
    result = dataloader.find_vars_files(path, name)
    assert result == []
