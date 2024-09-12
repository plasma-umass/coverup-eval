# file: lib/ansible/parsing/dataloader.py:116-118
# asked: {"lines": [117, 118], "branches": []}
# gained: {"lines": [117, 118], "branches": []}

import os
import pytest
from ansible.module_utils._text import to_bytes
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_directory_with_dwim_path(mocker, dataloader):
    mocker.patch.object(dataloader, 'path_dwim', return_value='/tmp')
    mocker.patch('os.path.isdir', return_value=True)
    
    result = dataloader.is_directory('some_path')
    
    dataloader.path_dwim.assert_called_once_with('some_path')
    assert result is True

def test_is_directory_with_non_dwim_path(mocker, dataloader):
    mocker.patch.object(dataloader, 'path_dwim', return_value='/nonexistent')
    mocker.patch('os.path.isdir', return_value=False)
    
    result = dataloader.is_directory('some_other_path')
    
    dataloader.path_dwim.assert_called_once_with('some_other_path')
    assert result is False
