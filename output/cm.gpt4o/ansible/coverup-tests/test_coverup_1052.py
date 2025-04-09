# file lib/ansible/plugins/lookup/fileglob.py:56-83
# lines [56, 58, 60, 61, 62, 63, 64, 65, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83]
# branches ['61->62', '61->83', '64->65', '64->68', '68->69', '68->71', '72->73', '72->76', '76->61', '76->77', '77->76', '77->78', '80->76', '80->81']

import os
import glob
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.lookup.fileglob import LookupModule

@pytest.fixture
def mock_glob(mocker):
    return mocker.patch('glob.glob')

@pytest.fixture
def mock_os_path_isfile(mocker):
    return mocker.patch('os.path.isfile')

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.plugins.lookup.fileglob.to_bytes', side_effect=lambda x, errors: x)

@pytest.fixture
def mock_to_text(mocker):
    return mocker.patch('ansible.plugins.lookup.fileglob.to_text', side_effect=lambda x, errors: x)

@pytest.fixture
def mock_find_file_in_search_path(mocker):
    return mocker.patch.object(LookupModule, 'find_file_in_search_path', return_value='/mocked/path')

@pytest.fixture
def mock_get_basedir(mocker):
    return mocker.patch.object(LookupModule, 'get_basedir', return_value='/mocked/basedir')

def test_run_with_directory_in_term(mock_glob, mock_os_path_isfile, mock_to_bytes, mock_to_text, mock_find_file_in_search_path):
    lookup = LookupModule()
    terms = ['/some/dir/file.txt']
    variables = {}

    mock_glob.return_value = ['/some/dir/file.txt']
    mock_os_path_isfile.return_value = True

    result = lookup.run(terms, variables)

    assert result == ['/some/dir/file.txt']
    mock_find_file_in_search_path.assert_called_once_with(variables, 'files', '/some/dir')
    mock_glob.assert_called_once_with('/mocked/path/file.txt')
    mock_os_path_isfile.assert_called_once_with('/some/dir/file.txt')

def test_run_without_directory_in_term(mock_glob, mock_os_path_isfile, mock_to_bytes, mock_to_text, mock_get_basedir):
    lookup = LookupModule()
    terms = ['file.txt']
    variables = {'ansible_search_path': ['/custom/path']}

    mock_glob.side_effect = [
        [],  # First call for '/custom/path/files/file.txt'
        ['/custom/path/file.txt']  # Second call for '/custom/path/file.txt'
    ]
    mock_os_path_isfile.return_value = True

    result = lookup.run(terms, variables)

    assert result == ['/custom/path/file.txt']
    mock_get_basedir.assert_not_called()
    mock_glob.assert_any_call('/custom/path/files/file.txt')
    mock_glob.assert_any_call('/custom/path/file.txt')
    mock_os_path_isfile.assert_called_once_with('/custom/path/file.txt')

def test_run_without_directory_in_term_no_search_path(mock_glob, mock_os_path_isfile, mock_to_bytes, mock_to_text, mock_get_basedir):
    lookup = LookupModule()
    terms = ['file.txt']
    variables = {}

    mock_glob.side_effect = [
        [],  # First call for '/mocked/basedir/files/file.txt'
        ['/mocked/basedir/file.txt']  # Second call for '/mocked/basedir/file.txt'
    ]
    mock_os_path_isfile.return_value = True

    result = lookup.run(terms, variables)

    assert result == ['/mocked/basedir/file.txt']
    mock_get_basedir.assert_called_once_with(variables)
    mock_glob.assert_any_call('/mocked/basedir/files/file.txt')
    mock_glob.assert_any_call('/mocked/basedir/file.txt')
    mock_os_path_isfile.assert_called_once_with('/mocked/basedir/file.txt')
