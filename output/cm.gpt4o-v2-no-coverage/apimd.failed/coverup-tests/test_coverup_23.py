# file: apimd/loader.py:109-145
# asked: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [126, 129], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}
# gained: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}

import pytest
from unittest.mock import patch, mock_open
from apimd.loader import gen_api, _site_path, loader, _write
from os import mkdir
from os.path import isdir, join
from sys import path as sys_path

@pytest.fixture
def mock_isdir(mocker):
    return mocker.patch('apimd.loader.isdir', return_value=False)

@pytest.fixture
def mock_mkdir(mocker):
    return mocker.patch('apimd.loader.mkdir')

@pytest.fixture
def mock_logger_info(mocker):
    return mocker.patch('apimd.logger.logger.info')

@pytest.fixture
def mock_logger_warning(mocker):
    return mocker.patch('apimd.logger.logger.warning')

@pytest.fixture
def mock_loader(mocker):
    return mocker.patch('apimd.loader.loader', return_value='doc content')

@pytest.fixture
def mock_write(mocker):
    return mocker.patch('apimd.loader._write')

@pytest.fixture
def mock_sys_path(mocker):
    original_sys_path = sys_path.copy()
    mocker.patch('sys.path', original_sys_path)
    return original_sys_path

def test_gen_api_creates_directory(mock_isdir, mock_mkdir, mock_logger_info, mock_loader, mock_write):
    root_names = {'Title': 'name'}
    result = gen_api(root_names, prefix='test_docs')
    mock_isdir.assert_called_once_with('test_docs')
    mock_mkdir.assert_called_once_with('test_docs')
    mock_logger_info.assert_any_call('Create directory: test_docs')
    assert len(result) == 1
    assert 'Title API' in result[0]

def test_gen_api_dry_run(mock_isdir, mock_mkdir, mock_logger_info, mock_loader, mock_write):
    root_names = {'Title': 'name'}
    result = gen_api(root_names, prefix='test_docs', dry=True)
    mock_isdir.assert_called_once_with('test_docs')
    mock_mkdir.assert_called_once_with('test_docs')
    mock_logger_info.assert_any_call('Create directory: test_docs')
    mock_write.assert_not_called()
    assert len(result) == 1
    assert 'Title API' in result[0]

def test_gen_api_with_pwd(mock_isdir, mock_mkdir, mock_logger_info, mock_loader, mock_write, mock_sys_path):
    root_names = {'Title': 'name'}
    result = gen_api(root_names, pwd='test_pwd', prefix='test_docs')
    assert 'test_pwd' in sys_path
    mock_isdir.assert_called_once_with('test_docs')
    mock_mkdir.assert_called_once_with('test_docs')
    mock_logger_info.assert_any_call('Create directory: test_docs')
    assert len(result) == 1
    assert 'Title API' in result[0]

def test_gen_api_loader_returns_empty(mock_isdir, mock_mkdir, mock_logger_info, mock_logger_warning, mock_loader, mock_write):
    mock_loader.return_value = ''
    root_names = {'Title': 'name'}
    result = gen_api(root_names, prefix='test_docs')
    mock_isdir.assert_called_once_with('test_docs')
    mock_mkdir.assert_called_once_with('test_docs')
    mock_logger_info.assert_any_call('Create directory: test_docs')
    mock_logger_warning.assert_called_once_with("'name' can not be found")
    assert len(result) == 0
