# file: apimd/loader.py:109-145
# asked: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [126, 129], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}
# gained: {"lines": [109, 111, 113, 114, 115, 116, 117, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145], "branches": [[124, 125], [124, 126], [126, 127], [126, 129], [130, 131], [130, 145], [133, 134], [133, 136], [139, 140], [139, 143]]}

import pytest
from unittest.mock import patch, mock_open
from apimd.loader import gen_api

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('apimd.loader.logger')

@pytest.fixture
def mock_isdir(mocker):
    return mocker.patch('apimd.loader.isdir')

@pytest.fixture
def mock_mkdir(mocker):
    return mocker.patch('apimd.loader.mkdir')

@pytest.fixture
def mock_sys_path(mocker):
    return mocker.patch('apimd.loader.sys_path', [])

@pytest.fixture
def mock_loader(mocker):
    return mocker.patch('apimd.loader.loader')

@pytest.fixture
def mock_site_path(mocker):
    return mocker.patch('apimd.loader._site_path')

@pytest.fixture
def mock_write(mocker):
    return mocker.patch('apimd.loader._write')

def test_gen_api_creates_directory(mock_logger, mock_isdir, mock_mkdir, mock_sys_path, mock_loader, mock_site_path, mock_write):
    mock_isdir.return_value = False
    mock_loader.return_value = "doc content"
    mock_site_path.return_value = "site_path"
    
    root_names = {"Title": "name"}
    docs = gen_api(root_names, pwd="some_path", prefix="docs", link=True, level=1, toc=False, dry=False)
    
    assert "# Title API\n\ndoc content" in docs
    mock_logger.info.assert_any_call("Create directory: docs")
    mock_mkdir.assert_called_once_with("docs")
    assert "some_path" in mock_sys_path

def test_gen_api_dry_run(mock_logger, mock_isdir, mock_mkdir, mock_sys_path, mock_loader, mock_site_path, mock_write):
    mock_isdir.return_value = True
    mock_loader.return_value = "doc content"
    mock_site_path.return_value = "site_path"
    
    root_names = {"Title": "name"}
    docs = gen_api(root_names, pwd=None, prefix="docs", link=True, level=1, toc=False, dry=True)
    
    assert "# Title API\n\ndoc content" in docs
    mock_write.assert_not_called()
    mock_logger.info.assert_any_call("============")
    mock_logger.info.assert_any_call("# Title API\n\ndoc content")

def test_gen_api_loader_empty_doc(mock_logger, mock_isdir, mock_mkdir, mock_sys_path, mock_loader, mock_site_path, mock_write):
    mock_isdir.return_value = True
    mock_loader.return_value = "   "
    mock_site_path.return_value = "site_path"
    
    root_names = {"Title": "name"}
    docs = gen_api(root_names, pwd=None, prefix="docs", link=True, level=1, toc=False, dry=False)
    
    assert docs == []
    mock_logger.warning.assert_any_call("'name' can not be found")
    mock_write.assert_not_called()

def test_gen_api_existing_directory(mock_logger, mock_isdir, mock_mkdir, mock_sys_path, mock_loader, mock_site_path, mock_write):
    mock_isdir.return_value = True
    mock_loader.return_value = "doc content"
    mock_site_path.return_value = "site_path"
    
    root_names = {"Title": "name"}
    docs = gen_api(root_names, pwd=None, prefix="docs", link=True, level=1, toc=False, dry=False)
    
    assert "# Title API\n\ndoc content" in docs
    mock_mkdir.assert_not_called()
    mock_write.assert_called_once_with("docs/name-api.md", "# Title API\n\ndoc content")
