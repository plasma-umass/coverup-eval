# file: lib/ansible/plugins/lookup/fileglob.py:56-83
# asked: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83], "branches": [[61, 62], [61, 83], [64, 65], [64, 68], [68, 69], [68, 71], [72, 73], [72, 76], [76, 61], [76, 77], [77, 76], [77, 78], [80, 76], [80, 81]]}
# gained: {"lines": [56, 58, 60, 61, 62, 63, 64, 65, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83], "branches": [[61, 62], [61, 83], [64, 65], [64, 68], [68, 69], [68, 71], [72, 73], [72, 76], [76, 77], [77, 78], [80, 81]]}

import os
import glob
import pytest
from ansible.plugins.lookup.fileglob import LookupModule
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_bytes, to_text

@pytest.fixture
def mock_glob(mocker):
    return mocker.patch('glob.glob')

@pytest.fixture
def mock_os_path_isfile(mocker):
    return mocker.patch('os.path.isfile')

@pytest.fixture
def mock_find_file_in_search_path(mocker):
    return mocker.patch.object(LookupModule, 'find_file_in_search_path')

@pytest.fixture
def mock_get_basedir(mocker):
    return mocker.patch.object(LookupModule, 'get_basedir')

@pytest.fixture
def setup_filesystem(tmpdir):
    base_dir = tmpdir.mkdir("basedir")
    files_dir = base_dir.mkdir("files")
    test_file = files_dir.join("testfile.txt")
    test_file.write("content")
    return str(base_dir), str(files_dir), str(test_file)

def test_run_with_directory_in_term(mock_glob, mock_os_path_isfile, mock_find_file_in_search_path, setup_filesystem):
    base_dir, files_dir, test_file = setup_filesystem
    mock_find_file_in_search_path.return_value = files_dir
    mock_glob.return_value = [to_bytes(test_file)]
    mock_os_path_isfile.return_value = True

    lookup = LookupModule()
    terms = [os.path.join(files_dir, "testfile.txt")]
    variables = {}

    result = lookup.run(terms, variables)

    assert result == [to_text(test_file)]
    mock_find_file_in_search_path.assert_called_once_with(variables, 'files', files_dir)
    mock_glob.assert_called_once_with(to_bytes(os.path.join(files_dir, "testfile.txt"), errors='surrogate_or_strict'))
    mock_os_path_isfile.assert_called_once_with(to_bytes(test_file))

def test_run_without_directory_in_term(mock_glob, mock_os_path_isfile, mock_get_basedir, setup_filesystem):
    base_dir, files_dir, test_file = setup_filesystem
    mock_get_basedir.return_value = base_dir
    mock_glob.return_value = [to_bytes(test_file)]
    mock_os_path_isfile.return_value = True

    lookup = LookupModule()
    terms = ["testfile.txt"]
    variables = {}

    result = lookup.run(terms, variables)

    assert result == [to_text(test_file)]
    mock_get_basedir.assert_called_once_with(variables)
    mock_glob.assert_called_once_with(to_bytes(os.path.join(files_dir, "testfile.txt"), errors='surrogate_or_strict'))
    mock_os_path_isfile.assert_called_once_with(to_bytes(test_file))

def test_run_with_ansible_search_path(mock_glob, mock_os_path_isfile, setup_filesystem):
    base_dir, files_dir, test_file = setup_filesystem
    mock_glob.return_value = [to_bytes(test_file)]
    mock_os_path_isfile.return_value = True

    lookup = LookupModule()
    terms = ["testfile.txt"]
    variables = {'ansible_search_path': [base_dir]}

    result = lookup.run(terms, variables)

    assert result == [to_text(test_file)]
    mock_glob.assert_called_once_with(to_bytes(os.path.join(files_dir, "testfile.txt"), errors='surrogate_or_strict'))
    mock_os_path_isfile.assert_called_once_with(to_bytes(test_file))
