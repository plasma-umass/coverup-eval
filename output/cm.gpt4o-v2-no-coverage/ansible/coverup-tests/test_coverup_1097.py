# file: lib/ansible/plugins/lookup/fileglob.py:56-83
# asked: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83], "branches": [[61, 62], [61, 83], [64, 65], [64, 68], [68, 69], [68, 71], [72, 73], [72, 76], [76, 61], [76, 77], [77, 76], [77, 78], [80, 76], [80, 81]]}
# gained: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83], "branches": [[61, 62], [61, 83], [64, 65], [64, 68], [68, 69], [68, 71], [72, 73], [72, 76], [76, 77], [77, 78], [80, 81]]}

import os
import glob
import pytest
from unittest.mock import patch, MagicMock
from ansible.plugins.lookup.fileglob import LookupModule
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def mock_glob(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(glob, 'glob', mock)
    return mock

@pytest.fixture
def mock_isfile(monkeypatch):
    mock = MagicMock(return_value=True)
    monkeypatch.setattr(os.path, 'isfile', mock)
    return mock

@pytest.fixture
def mock_find_file_in_search_path(monkeypatch):
    mock = MagicMock(return_value='/mocked/path')
    monkeypatch.setattr(LookupModule, 'find_file_in_search_path', mock)
    return mock

@pytest.fixture
def mock_get_basedir(monkeypatch):
    mock = MagicMock(return_value='/mocked/basedir')
    monkeypatch.setattr(LookupModule, 'get_basedir', mock)
    return mock

def test_run_with_directory_in_term(mock_glob, mock_isfile, mock_find_file_in_search_path):
    lookup = LookupModule()
    terms = ['/some/dir/file.txt']
    variables = {}
    mock_glob.return_value = [to_bytes('/mocked/path/file.txt')]
    
    result = lookup.run(terms, variables)
    
    mock_find_file_in_search_path.assert_called_once_with(variables, 'files', '/some/dir')
    mock_glob.assert_called_once_with(to_bytes('/mocked/path/file.txt', errors='surrogate_or_strict'))
    assert result == ['/mocked/path/file.txt']

def test_run_without_directory_in_term(mock_glob, mock_isfile, mock_get_basedir):
    lookup = LookupModule()
    terms = ['file.txt']
    variables = {}
    mock_glob.return_value = [to_bytes('/mocked/basedir/files/file.txt')]
    
    result = lookup.run(terms, variables)
    
    mock_get_basedir.assert_called_once_with(variables)
    mock_glob.assert_called_once_with(to_bytes('/mocked/basedir/files/file.txt', errors='surrogate_or_strict'))
    assert result == ['/mocked/basedir/files/file.txt']

def test_run_with_ansible_search_path(mock_glob, mock_isfile):
    lookup = LookupModule()
    terms = ['file.txt']
    variables = {'ansible_search_path': ['/custom/path']}
    mock_glob.return_value = [to_bytes('/custom/path/files/file.txt')]
    
    result = lookup.run(terms, variables)
    
    mock_glob.assert_called_once_with(to_bytes('/custom/path/files/file.txt', errors='surrogate_or_strict'))
    assert result == ['/custom/path/files/file.txt']
