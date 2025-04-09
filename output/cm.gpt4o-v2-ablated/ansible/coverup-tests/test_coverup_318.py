# file: lib/ansible/parsing/dataloader.py:116-118
# asked: {"lines": [116, 117, 118], "branches": []}
# gained: {"lines": [116, 117, 118], "branches": []}

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_directory_with_existing_directory(dataloader, mocker):
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/existing/directory')
    mocker.patch('os.path.isdir', return_value=True)
    assert dataloader.is_directory('/some/path') is True

def test_is_directory_with_non_existing_directory(dataloader, mocker):
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/non/existing/directory')
    mocker.patch('os.path.isdir', return_value=False)
    assert dataloader.is_directory('/some/path') is False

def test_is_directory_with_bytes_conversion_error(dataloader, mocker):
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/some/path')
    mocker.patch('os.path.isdir', side_effect=UnicodeEncodeError('codec', 'input', 0, 1, 'reason'))
    with pytest.raises(UnicodeEncodeError):
        dataloader.is_directory('/some/path')
