# file lib/ansible/parsing/dataloader.py:420-452
# lines [439]
# branches ['438->439']

import os
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def to_bytes(path):
    return path.encode('utf-8')

def to_text(path):
    return path.decode('utf-8')

@pytest.fixture
def mock_os_path(mocker):
    mocker.patch('os.path.join', side_effect=lambda *args: '/'.join(args))
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.path.isdir', return_value=False)

def test_find_vars_files_with_extension(dataloader, mock_os_path, mocker):
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=False)
    
    path = 'some/path'
    name = 'vars'
    extensions = ['yml', 'yaml']
    
    result = dataloader.find_vars_files(path, name, extensions)
    
    expected_path = to_bytes(os.path.join(path, name)) + b'.' + to_bytes('yml')
    assert expected_path in result

def test_find_vars_files_cleanup(dataloader, mock_os_path, mocker):
    mocker.patch.object(dataloader, 'path_exists', return_value=True)
    mocker.patch.object(dataloader, 'is_directory', return_value=False)
    
    path = 'some/path'
    name = 'vars'
    extensions = ['yml', 'yaml']
    
    result = dataloader.find_vars_files(path, name, extensions)
    
    expected_path = to_bytes(os.path.join(path, name)) + b'.' + to_bytes('yml')
    assert expected_path in result
    assert len(result) == 1
