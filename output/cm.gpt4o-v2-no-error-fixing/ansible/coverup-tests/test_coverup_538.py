# file: lib/ansible/parsing/dataloader.py:108-110
# asked: {"lines": [108, 109, 110], "branches": []}
# gained: {"lines": [108, 109, 110], "branches": []}

import os
import pytest
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_bytes

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_exists_with_absolute_path(mocker, dataloader):
    mocker.patch.object(dataloader, '_basedir', '/base/dir')
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/absolute/path')

    path = '/absolute/path'
    result = dataloader.path_exists(path)

    dataloader.path_dwim.assert_called_once_with(path)
    os.path.exists.assert_called_once_with(to_bytes('/absolute/path', errors='surrogate_or_strict'))
    assert result is True

def test_path_exists_with_relative_path(mocker, dataloader):
    mocker.patch.object(dataloader, '_basedir', '/base/dir')
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('ansible.parsing.dataloader.DataLoader.path_dwim', return_value='/base/dir/relative/path')

    path = 'relative/path'
    result = dataloader.path_exists(path)

    dataloader.path_dwim.assert_called_once_with(path)
    os.path.exists.assert_called_once_with(to_bytes('/base/dir/relative/path', errors='surrogate_or_strict'))
    assert result is False
