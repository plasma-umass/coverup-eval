# file: lib/ansible/parsing/dataloader.py:120-122
# asked: {"lines": [120, 121, 122], "branches": []}
# gained: {"lines": [120, 121, 122], "branches": []}

import os
import pytest
from unittest.mock import patch, MagicMock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_list_directory_with_absolute_path(dataloader):
    with patch('ansible.parsing.dataloader.os.listdir') as mock_listdir, \
         patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/absolute/path') as mock_path_dwim:
        
        mock_listdir.return_value = ['file1', 'file2']
        
        result = dataloader.list_directory('/absolute/path')
        
        mock_path_dwim.assert_called_once_with('/absolute/path')
        mock_listdir.assert_called_once_with('/absolute/path')
        assert result == ['file1', 'file2']

def test_list_directory_with_relative_path(dataloader):
    with patch('ansible.parsing.dataloader.os.listdir') as mock_listdir, \
         patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/base/dir/relative/path') as mock_path_dwim:
        
        mock_listdir.return_value = ['file1', 'file2']
        
        result = dataloader.list_directory('relative/path')
        
        mock_path_dwim.assert_called_once_with('relative/path')
        mock_listdir.assert_called_once_with('/base/dir/relative/path')
        assert result == ['file1', 'file2']
