# file lib/ansible/config/manager.py:49-158
# lines [78, 97, 100, 101, 103, 104, 110, 116, 121, 130, 139, 143, 149, 156]
# branches ['77->78', '96->97', '99->100', '100->101', '100->103', '103->104', '103->155', '107->110', '113->121', '115->116', '124->127', '127->130', '133->136', '136->139', '142->143', '146->149', '155->156']

import os
import tempfile
import pytest
from unittest.mock import patch, MagicMock
from ansible.config.manager import ensure_type

@pytest.fixture
def mock_os_path_isabs(mocker):
    return mocker.patch('os.path.isabs', return_value=True)

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists', return_value=True)

@pytest.fixture
def mock_resolve_path(mocker):
    return mocker.patch('ansible.config.manager.resolve_path', side_effect=lambda x, basedir=None: x)

@pytest.fixture
def mock_makedirs_safe(mocker):
    return mocker.patch('ansible.config.manager.makedirs_safe')

@pytest.fixture
def mock_tempfile_mkdtemp(mocker):
    return mocker.patch('tempfile.mkdtemp', return_value='/tmp/ansible-local-12345')

@pytest.fixture
def mock_atexit_register(mocker):
    return mocker.patch('atexit.register')

def test_ensure_type_path(mock_os_path_isabs, mock_os_path_exists, mock_resolve_path):
    result = ensure_type('/some/path', 'path', origin='/origin/path')
    assert result == '/some/path'

def test_ensure_type_tmppath(mock_os_path_isabs, mock_os_path_exists, mock_resolve_path, mock_makedirs_safe, mock_tempfile_mkdtemp, mock_atexit_register):
    mock_os_path_exists.side_effect = lambda x: x != '/some/path'
    result = ensure_type('/some/path', 'tmppath', origin='/origin/path')
    assert result == '/tmp/ansible-local-12345'
    mock_makedirs_safe.assert_called_once_with('/some/path', 0o700)
    mock_atexit_register.assert_called_once()

def test_ensure_type_none():
    result = ensure_type('None', 'none')
    assert result is None

    with pytest.raises(ValueError, match='Invalid type provided for "None"'):
        ensure_type('not_none', 'none')

def test_ensure_type_list():
    result = ensure_type('a,b,c', 'list')
    assert result == ['a', 'b', 'c']

    with pytest.raises(ValueError, match='Invalid type provided for "list"'):
        ensure_type(123, 'list')

def test_ensure_type_pathspec(mock_resolve_path):
    result = ensure_type('/path1:/path2', 'pathspec', origin='/origin/path')
    assert result == ['/path1', '/path2']

    with pytest.raises(ValueError, match='Invalid type provided for "pathspec"'):
        ensure_type(123, 'pathspec')

def test_ensure_type_pathlist(mock_resolve_path):
    result = ensure_type('/path1,/path2', 'pathlist', origin='/origin/path')
    assert result == ['/path1', '/path2']

    with pytest.raises(ValueError, match='Invalid type provided for "pathlist"'):
        ensure_type(123, 'pathlist')

def test_ensure_type_dictionary():
    with pytest.raises(ValueError, match='Invalid type provided for "dictionary"'):
        ensure_type('not_a_dict', 'dictionary')

def test_ensure_type_string():
    result = ensure_type(123, 'string')
    assert result == '123'

    with pytest.raises(ValueError, match='Invalid type provided for "string"'):
        ensure_type([], 'string')
