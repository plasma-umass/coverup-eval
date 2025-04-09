# file: apimd/loader.py:109-145
# asked: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [126, 129], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}
# gained: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}

import pytest
from unittest.mock import patch, mock_open
from apimd.loader import gen_api

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('apimd.loader.logger')

@pytest.fixture
def mock_isdir(mocker):
    return mocker.patch('apimd.loader.isdir', return_value=False)

@pytest.fixture
def mock_mkdir(mocker):
    return mocker.patch('apimd.loader.mkdir')

@pytest.fixture
def mock_sys_path(mocker):
    return mocker.patch('apimd.loader.sys_path', [])

@pytest.fixture
def mock_loader(mocker):
    return mocker.patch('apimd.loader.loader', return_value='doc content')

@pytest.fixture
def mock_site_path(mocker):
    return mocker.patch('apimd.loader._site_path', return_value='/mock/site/path')

@pytest.fixture
def mock_write(mocker):
    return mocker.patch('apimd.loader._write')

def test_gen_api_creates_directory(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path, mock_write):
    root_names = {'Title': 'name'}
    result = gen_api(root_names, prefix='mock_prefix')
    
    mock_isdir.assert_called_once_with('mock_prefix')
    mock_mkdir.assert_called_once_with('mock_prefix')
    mock_logger.info.assert_any_call('Create directory: mock_prefix')
    mock_logger.info.assert_any_call('Load root: name (Title)')
    mock_logger.info.assert_any_call('Write file: mock_prefix/name-api.md')
    mock_write.assert_called_once_with('mock_prefix/name-api.md', '# Title API\n\ndoc content')
    assert result == ['# Title API\n\ndoc content']

def test_gen_api_dry_run(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path):
    root_names = {'Title': 'name'}
    result = gen_api(root_names, prefix='mock_prefix', dry=True)
    
    mock_isdir.assert_called_once_with('mock_prefix')
    mock_mkdir.assert_called_once_with('mock_prefix')
    mock_logger.info.assert_any_call('Create directory: mock_prefix')
    mock_logger.info.assert_any_call('Load root: name (Title)')
    mock_logger.info.assert_any_call('Write file: mock_prefix/name-api.md')
    mock_logger.info.assert_any_call('=' * 12)
    mock_logger.info.assert_any_call('# Title API\n\ndoc content')
    assert result == ['# Title API\n\ndoc content']

def test_gen_api_with_pwd(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path, mock_write, mock_sys_path):
    root_names = {'Title': 'name'}
    result = gen_api(root_names, pwd='/mock/pwd', prefix='mock_prefix')
    
    assert '/mock/pwd' in mock_sys_path
    mock_isdir.assert_called_once_with('mock_prefix')
    mock_mkdir.assert_called_once_with('mock_prefix')
    mock_logger.info.assert_any_call('Create directory: mock_prefix')
    mock_logger.info.assert_any_call('Load root: name (Title)')
    mock_logger.info.assert_any_call('Write file: mock_prefix/name-api.md')
    mock_write.assert_called_once_with('mock_prefix/name-api.md', '# Title API\n\ndoc content')
    assert result == ['# Title API\n\ndoc content']

def test_gen_api_loader_returns_empty(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path):
    mock_loader.return_value = ''
    root_names = {'Title': 'name'}
    result = gen_api(root_names, prefix='mock_prefix')
    
    mock_isdir.assert_called_once_with('mock_prefix')
    mock_mkdir.assert_called_once_with('mock_prefix')
    mock_logger.info.assert_any_call('Create directory: mock_prefix')
    mock_logger.info.assert_any_call('Load root: name (Title)')
    mock_logger.warning.assert_any_call("'name' can not be found")
    assert result == []
