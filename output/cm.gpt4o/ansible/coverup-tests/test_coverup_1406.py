# file lib/ansible/cli/arguments/option_helpers.py:112-152
# lines [123, 126, 127, 133, 140, 141, 142, 148]
# branches ['122->123', '130->133', '134->140', '145->148']

import os
import pytest
import time
from unittest import mock
from ansible.cli.arguments.option_helpers import _git_repo_info

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_os_path_isfile(mocker):
    return mocker.patch('os.path.isfile')

@pytest.fixture
def mock_os_stat(mocker):
    return mocker.patch('os.stat')

@pytest.fixture
def mock_open(mocker):
    return mocker.patch('builtins.open', mock.mock_open(read_data='ref: refs/heads/main\n'))

@pytest.fixture
def mock_yaml_load(mocker):
    return mocker.patch('ansible.cli.arguments.option_helpers.yaml_load', return_value={'gitdir': '/absolute/path/to/.git'})

def test_git_repo_info_absolute_gitdir(mock_os_path_exists, mock_os_path_isfile, mock_os_stat, mock_open, mock_yaml_load):
    mock_os_path_exists.side_effect = lambda path: True
    mock_os_path_isfile.side_effect = lambda path: path.endswith('.git')
    mock_os_stat.return_value.st_mtime = time.time()

    repo_path = '/path/to/repo/.git'
    result = _git_repo_info(repo_path)

    assert result.startswith('(main ')
    assert 'last updated' in result
    assert 'GMT' in result

def test_git_repo_info_relative_gitdir(mock_os_path_exists, mock_os_path_isfile, mock_os_stat, mock_open, mock_yaml_load):
    mock_yaml_load.return_value = {'gitdir': 'relative/path/to/.git'}
    mock_os_path_exists.side_effect = lambda path: True
    mock_os_path_isfile.side_effect = lambda path: path.endswith('.git')
    mock_os_stat.return_value.st_mtime = time.time()

    repo_path = '/path/to/repo/.git'
    result = _git_repo_info(repo_path)

    assert result.startswith('(main ')
    assert 'last updated' in result
    assert 'GMT' in result

def test_git_repo_info_detached_head(mock_os_path_exists, mock_os_path_isfile, mock_os_stat, mock_open):
    mock_open.return_value = mock.mock_open(read_data='commit_hash\n').return_value
    mock_os_path_exists.side_effect = lambda path: True
    mock_os_path_isfile.side_effect = lambda path: False
    mock_os_stat.return_value.st_mtime = time.time()

    repo_path = '/path/to/repo/.git'
    result = _git_repo_info(repo_path)

    assert result.startswith('(detached HEAD ')
    assert 'last updated' in result
    assert 'GMT' in result

def test_git_repo_info_ioerror(mock_os_path_exists, mock_os_path_isfile, mock_open):
    mock_open.side_effect = IOError
    mock_os_path_exists.side_effect = lambda path: True
    mock_os_path_isfile.side_effect = lambda path: path.endswith('.git')

    repo_path = '/path/to/repo/.git'
    result = _git_repo_info(repo_path)

    assert result == ''
