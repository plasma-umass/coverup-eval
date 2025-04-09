# file: apimd/loader.py:109-145
# asked: {"lines": [], "branches": [[126, 129]]}
# gained: {"lines": [], "branches": [[126, 129]]}

import pytest
import os
from unittest.mock import patch, MagicMock
from apimd.loader import gen_api

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('apimd.loader.logger')

@pytest.fixture
def mock_loader(mocker):
    return mocker.patch('apimd.loader.loader', return_value="Some documentation")

@pytest.fixture
def mock_write(mocker):
    return mocker.patch('apimd.loader._write')

@pytest.fixture
def mock_isdir(mocker):
    return mocker.patch('apimd.loader.isdir')

@pytest.fixture
def mock_mkdir(mocker):
    return mocker.patch('apimd.loader.mkdir')

@pytest.fixture
def mock_sys_path(mocker):
    return mocker.patch('apimd.loader.sys_path', [])

def test_gen_api_creates_directory(mock_logger, mock_loader, mock_write, mock_isdir, mock_mkdir, mock_sys_path):
    mock_isdir.return_value = False
    root_names = {'Title': 'module_name'}
    prefix = 'docs'
    result = gen_api(root_names, prefix=prefix)
    
    mock_isdir.assert_called_once_with(prefix)
    mock_mkdir.assert_called_once_with(prefix)
    mock_logger.info.assert_any_call(f"Create directory: {prefix}")
    assert len(result) == 1
    assert "Some documentation" in result[0]

def test_gen_api_does_not_create_directory_if_exists(mock_logger, mock_loader, mock_write, mock_isdir, mock_mkdir, mock_sys_path):
    mock_isdir.return_value = True
    root_names = {'Title': 'module_name'}
    prefix = 'docs'
    
    result = gen_api(root_names, prefix=prefix)
    
    mock_isdir.assert_called_once_with(prefix)
    mock_mkdir.assert_not_called()
    assert len(result) == 1
    assert "Some documentation" in result[0]
