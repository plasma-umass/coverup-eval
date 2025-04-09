# file: lib/ansible/parsing/dataloader.py:454-468
# asked: {"lines": [455, 456, 457, 459, 460, 462, 463, 464, 466, 468], "branches": [[456, 457], [456, 468], [457, 456], [457, 459], [462, 463], [462, 464], [464, 456], [464, 466]]}
# gained: {"lines": [455, 456, 457, 459, 460, 462, 463, 464, 466, 468], "branches": [[456, 457], [456, 468], [457, 456], [457, 459], [462, 463], [462, 464], [464, 456], [464, 466]]}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_get_dir_vars_files_no_hidden_no_backup(dataloader):
    with patch.object(dataloader, 'list_directory', return_value=['file1.yml', 'file2.txt', '.hidden', 'backup~']), \
         patch.object(dataloader, 'is_directory', side_effect=lambda x: False), \
         patch.object(dataloader, 'is_file', side_effect=lambda x: True):
        
        result = dataloader._get_dir_vars_files('/some/path', ['.yml', '.txt'])
        assert result == ['/some/path/file1.yml', '/some/path/file2.txt']

def test_get_dir_vars_files_with_directory(dataloader):
    with patch.object(dataloader, 'list_directory', side_effect=[['dir1', 'file1.yml'], ['file2.txt']]), \
         patch.object(dataloader, 'is_directory', side_effect=lambda x: x.endswith('dir1')), \
         patch.object(dataloader, 'is_file', side_effect=lambda x: not x.endswith('dir1')):
        
        result = dataloader._get_dir_vars_files('/some/path', ['.yml', '.txt'])
        assert result == ['/some/path/dir1/file2.txt', '/some/path/file1.yml']

def test_get_dir_vars_files_with_invalid_extension(dataloader):
    with patch.object(dataloader, 'list_directory', return_value=['file1.invalid', 'file2.yml']), \
         patch.object(dataloader, 'is_directory', side_effect=lambda x: False), \
         patch.object(dataloader, 'is_file', side_effect=lambda x: True):
        
        result = dataloader._get_dir_vars_files('/some/path', ['.yml'])
        assert result == ['/some/path/file2.yml']
