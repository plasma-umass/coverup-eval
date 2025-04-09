# file: lib/ansible/parsing/dataloader.py:116-118
# asked: {"lines": [116, 117, 118], "branches": []}
# gained: {"lines": [116, 117, 118], "branches": []}

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_directory_with_absolute_path(mocker, dataloader):
    mocker.patch.object(dataloader, 'path_dwim', return_value='/tmp')
    mocker.patch('os.path.isdir', return_value=True)
    
    result = dataloader.is_directory('/tmp')
    
    assert result is True
    dataloader.path_dwim.assert_called_once_with('/tmp')
    os.path.isdir.assert_called_once_with(to_bytes('/tmp', errors='surrogate_or_strict'))

def test_is_directory_with_relative_path(mocker, dataloader):
    mocker.patch.object(dataloader, 'path_dwim', return_value='relative_path')
    mocker.patch('os.path.isdir', return_value=False)
    
    result = dataloader.is_directory('relative_path')
    
    assert result is False
    dataloader.path_dwim.assert_called_once_with('relative_path')
    os.path.isdir.assert_called_once_with(to_bytes('relative_path', errors='surrogate_or_strict'))
