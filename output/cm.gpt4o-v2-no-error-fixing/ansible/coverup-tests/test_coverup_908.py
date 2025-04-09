# file: lib/ansible/module_utils/facts/system/distribution.py:30-44
# asked: {"lines": [37, 41], "branches": [[36, 37], [40, 41]]}
# gained: {"lines": [37, 41], "branches": [[36, 37], [40, 41]]}

import os
import pytest
from unittest import mock

from ansible.module_utils.facts.system.distribution import _file_exists

@pytest.fixture
def mock_os_path_exists():
    with mock.patch('os.path.exists') as mock_exists:
        yield mock_exists

@pytest.fixture
def mock_os_path_getsize():
    with mock.patch('os.path.getsize') as mock_getsize:
        yield mock_getsize

def test_file_exists_path_does_not_exist(mock_os_path_exists):
    mock_os_path_exists.return_value = False
    assert not _file_exists('/non/existent/path')

def test_file_exists_allow_empty(mock_os_path_exists):
    mock_os_path_exists.return_value = True
    assert _file_exists('/some/path', allow_empty=True)

def test_file_exists_empty_file_not_allowed(mock_os_path_exists, mock_os_path_getsize):
    mock_os_path_exists.return_value = True
    mock_os_path_getsize.return_value = 0
    assert not _file_exists('/some/path', allow_empty=False)

def test_file_exists_non_empty_file(mock_os_path_exists, mock_os_path_getsize):
    mock_os_path_exists.return_value = True
    mock_os_path_getsize.return_value = 10
    assert _file_exists('/some/path', allow_empty=False)
