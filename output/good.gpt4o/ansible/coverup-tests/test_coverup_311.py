# file lib/ansible/module_utils/facts/system/distribution.py:30-44
# lines [30, 32, 33, 36, 37, 40, 41, 44]
# branches ['32->33', '32->36', '36->37', '36->40', '40->41', '40->44']

import os
import pytest
from unittest import mock

# Assuming the function _file_exists is part of a class or module, we need to import it correctly.
# For this example, let's assume it's part of a module named 'distribution'.
from ansible.module_utils.facts.system.distribution import _file_exists

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_os_path_getsize(mocker):
    return mocker.patch('os.path.getsize')

def test_file_exists_not_found(mock_os_path_exists):
    mock_os_path_exists.return_value = False
    assert not _file_exists('/non/existent/path')

def test_file_exists_allow_empty(mock_os_path_exists):
    mock_os_path_exists.return_value = True
    assert _file_exists('/some/path', allow_empty=True)

def test_file_exists_empty_not_allowed(mock_os_path_exists, mock_os_path_getsize):
    mock_os_path_exists.return_value = True
    mock_os_path_getsize.return_value = 0
    assert not _file_exists('/some/path', allow_empty=False)

def test_file_exists_with_content(mock_os_path_exists, mock_os_path_getsize):
    mock_os_path_exists.return_value = True
    mock_os_path_getsize.return_value = 100
    assert _file_exists('/some/path', allow_empty=False)
