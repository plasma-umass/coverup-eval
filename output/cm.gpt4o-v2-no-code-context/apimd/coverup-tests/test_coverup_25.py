# file: apimd/loader.py:109-145
# asked: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [126, 129], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}
# gained: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}

import pytest
from unittest.mock import patch, mock_open, MagicMock
from apimd.loader import gen_api
import os

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('apimd.loader.logger')

@pytest.fixture
def mock_loader(mocker):
    return mocker.patch('apimd.loader.loader', return_value="Mocked doc content")

@pytest.fixture
def mock_isdir(mocker):
    return mocker.patch('apimd.loader.isdir', return_value=False)

@pytest.fixture
def mock_mkdir(mocker):
    return mocker.patch('apimd.loader.mkdir')

@pytest.fixture
def mock_write(mocker):
    return mocker.patch('apimd.loader._write')

@pytest.fixture
def mock_sys_path(mocker):
    return mocker.patch('apimd.loader.sys_path', [])

@pytest.fixture
def mock_site_path(mocker):
    return mocker.patch('apimd.loader._site_path', return_value='/mock/site_path/module_name')

def test_gen_api_with_pwd(mock_logger, mock_loader, mock_isdir, mock_mkdir, mock_write, mock_sys_path, mock_site_path):
    root_names = {'Title': 'module_name'}
    pwd = '/mock/path'
    result = gen_api(root_names, pwd=pwd)

    assert mock_sys_path == [pwd]
    mock_mkdir.assert_called_once_with('docs')
    mock_loader.assert_called_once_with('module_name', '/mock/site_path/module_name', True, 1, False)
    mock_write.assert_called_once()
    assert result == ['# Title API\n\nMocked doc content']

def test_gen_api_without_pwd(mock_logger, mock_loader, mock_isdir, mock_mkdir, mock_write, mock_site_path):
    root_names = {'Title': 'module_name'}
    result = gen_api(root_names)

    mock_mkdir.assert_called_once_with('docs')
    mock_loader.assert_called_once_with('module_name', '/mock/site_path/module_name', True, 1, False)
    mock_write.assert_called_once()
    assert result == ['# Title API\n\nMocked doc content']

def test_gen_api_dry_run(mock_logger, mock_loader, mock_isdir, mock_mkdir, mock_site_path):
    root_names = {'Title': 'module_name'}
    result = gen_api(root_names, dry=True)

    mock_mkdir.assert_called_once_with('docs')
    mock_loader.assert_called_once_with('module_name', '/mock/site_path/module_name', True, 1, False)
    mock_logger.info.assert_any_call('=' * 12)
    mock_logger.info.assert_any_call('# Title API\n\nMocked doc content')
    assert result == ['# Title API\n\nMocked doc content']

def test_gen_api_empty_doc(mock_logger, mock_isdir, mock_mkdir, mock_write, mock_site_path):
    with patch('apimd.loader.loader', return_value="") as mock_loader:
        root_names = {'Title': 'module_name'}
        result = gen_api(root_names)

        mock_mkdir.assert_called_once_with('docs')
        mock_loader.assert_called_once_with('module_name', '/mock/site_path/module_name', True, 1, False)
        mock_logger.warning.assert_called_once_with("'module_name' can not be found")
        mock_write.assert_not_called()
        assert result == []
