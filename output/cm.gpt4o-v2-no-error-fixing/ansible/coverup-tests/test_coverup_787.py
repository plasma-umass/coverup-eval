# file: lib/ansible/module_utils/facts/utils.py:23-60
# asked: {"lines": [42, 43, 52, 54, 56], "branches": [[34, 60], [48, 51], [51, 52]]}
# gained: {"lines": [52], "branches": [[34, 60], [48, 51], [51, 52]]}

import pytest
import os
import fcntl
from unittest import mock
from ansible.module_utils.facts.utils import get_file_content

def test_get_file_content_file_exists_and_readable(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.access', return_value=True)
    mock_open = mocker.mock_open(read_data=' file content ')
    mocker.patch('builtins.open', mock_open)
    mocker.patch('fcntl.fcntl', side_effect=[0, 0])

    result = get_file_content('/fake/path', default='default content', strip=True)
    assert result == 'file content'
    mock_open.assert_called_once_with('/fake/path')
    fcntl.fcntl.assert_any_call(mock_open().fileno(), fcntl.F_GETFL)
    fcntl.fcntl.assert_any_call(mock_open().fileno(), fcntl.F_SETFL, 0 | os.O_NONBLOCK)

def test_get_file_content_file_exists_and_readable_no_strip(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.access', return_value=True)
    mock_open = mocker.mock_open(read_data=' file content ')
    mocker.patch('builtins.open', mock_open)
    mocker.patch('fcntl.fcntl', side_effect=[0, 0])

    result = get_file_content('/fake/path', default='default content', strip=False)
    assert result == ' file content '
    mock_open.assert_called_once_with('/fake/path')
    fcntl.fcntl.assert_any_call(mock_open().fileno(), fcntl.F_GETFL)
    fcntl.fcntl.assert_any_call(mock_open().fileno(), fcntl.F_SETFL, 0 | os.O_NONBLOCK)

def test_get_file_content_file_exists_and_readable_empty_file(mocker):
    mocker.patch('os.path.exists', return_value=True)
    mocker.patch('os.access', return_value=True)
    mock_open = mocker.mock_open(read_data='')
    mocker.patch('builtins.open', mock_open)
    mocker.patch('fcntl.fcntl', side_effect=[0, 0])

    result = get_file_content('/fake/path', default='default content', strip=True)
    assert result == 'default content'
    mock_open.assert_called_once_with('/fake/path')
    fcntl.fcntl.assert_any_call(mock_open().fileno(), fcntl.F_GETFL)
    fcntl.fcntl.assert_any_call(mock_open().fileno(), fcntl.F_SETFL, 0 | os.O_NONBLOCK)

def test_get_file_content_file_not_exists(mocker):
    mocker.patch('os.path.exists', return_value=False)
    mocker.patch('os.access', return_value=False)

    result = get_file_content('/fake/path', default='default content', strip=True)
    assert result == 'default content'
