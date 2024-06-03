# file lib/ansible/parsing/dataloader.py:420-452
# lines [420, 427, 428, 430, 432, 434, 436, 437, 438, 439, 441, 443, 444, 445, 446, 448, 450, 451, 452]
# branches ['430->432', '430->434', '434->436', '434->452', '436->437', '436->438', '438->439', '438->441', '443->434', '443->444', '444->445', '444->450', '445->446', '445->448']

import os
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes, to_text
import ansible.constants as C

@pytest.fixture
def dataloader():
    return DataLoader()

def test_find_vars_files_no_extension(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = None

    b_path = to_bytes(os.path.join(path, name))
    mocker.patch.object(dataloader, 'path_exists', side_effect=lambda p: p == b_path)
    mocker.patch.object(dataloader, 'is_directory', return_value=False)

    result = dataloader.find_vars_files(path, name, extensions)
    assert result == [b_path]

def test_find_vars_files_with_extension(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = ['.yml']

    b_path = to_bytes(os.path.join(path, name))
    full_path = b_path + to_bytes('.yml')
    mocker.patch.object(dataloader, 'path_exists', side_effect=lambda p: p == full_path)
    mocker.patch.object(dataloader, 'is_directory', return_value=False)

    result = dataloader.find_vars_files(path, name, extensions)
    assert result == [full_path]

def test_find_vars_files_directory_allowed(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = None

    b_path = to_bytes(os.path.join(path, name))
    mocker.patch.object(dataloader, 'path_exists', side_effect=lambda p: p == b_path)
    mocker.patch.object(dataloader, 'is_directory', return_value=True)
    mocker.patch.object(dataloader, '_get_dir_vars_files', return_value=[to_text(b_path)])

    result = dataloader.find_vars_files(path, name, extensions)
    assert result == [to_text(b_path)]

def test_find_vars_files_directory_not_allowed(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = None

    b_path = to_bytes(os.path.join(path, name))
    mocker.patch.object(dataloader, 'path_exists', side_effect=lambda p: p == b_path)
    mocker.patch.object(dataloader, 'is_directory', return_value=True)

    result = dataloader.find_vars_files(path, name, extensions, allow_dir=False)
    assert result == []

def test_find_vars_files_with_multiple_extensions(dataloader, mocker):
    path = '/some/path'
    name = 'vars'
    extensions = ['.yml', '.yaml']

    b_path = to_bytes(os.path.join(path, name))
    full_path_yml = b_path + to_bytes('.yml')
    full_path_yaml = b_path + to_bytes('.yaml')
    mocker.patch.object(dataloader, 'path_exists', side_effect=lambda p: p in [full_path_yml, full_path_yaml])
    mocker.patch.object(dataloader, 'is_directory', return_value=False)

    result = dataloader.find_vars_files(path, name, extensions)
    assert result == [full_path_yml]
