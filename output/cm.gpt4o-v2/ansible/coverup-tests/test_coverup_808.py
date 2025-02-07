# file: lib/ansible/parsing/dataloader.py:120-122
# asked: {"lines": [120, 121, 122], "branches": []}
# gained: {"lines": [120, 121, 122], "branches": []}

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_list_directory_with_absolute_path(dataloader):
    with patch.object(dataloader, 'path_dwim', return_value='/tmp'), \
         patch('os.listdir', return_value=['file1', 'file2']) as mock_listdir:
        result = dataloader.list_directory('/tmp')
        assert result == ['file1', 'file2']
        mock_listdir.assert_called_once_with('/tmp')

def test_list_directory_with_relative_path(dataloader):
    with patch.object(dataloader, 'path_dwim', return_value='/tmp'), \
         patch('os.listdir', return_value=['file1', 'file2']) as mock_listdir:
        result = dataloader.list_directory('relative/path')
        assert result == ['file1', 'file2']
        mock_listdir.assert_called_once_with('/tmp')
