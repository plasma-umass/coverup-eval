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

def test_gen_api_creates_directory(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path, mock_write):
    mock_isdir.return_value = False
    mock_loader.return_value = "some documentation"
    mock_site_path.return_value = "some/path"

    root_names = {"Title": "name"}
    result = gen_api(root_names, prefix="test_docs")

    mock_isdir.assert_called_once_with("test_docs")
    mock_mkdir.assert_called_once_with("test_docs")
    assert len(result) == 1
    assert "some documentation" in result[0]

def test_gen_api_dry_run(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path, mock_write):
    mock_isdir.return_value = True
    mock_loader.return_value = "some documentation"
    mock_site_path.return_value = "some/path"

    root_names = {"Title": "name"}
    result = gen_api(root_names, prefix="test_docs", dry=True)

    mock_isdir.assert_called_once_with("test_docs")
    mock_mkdir.assert_not_called()
    mock_write.assert_not_called()
    assert len(result) == 1
    assert "some documentation" in result[0]

def test_gen_api_handles_empty_doc(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path, mock_write):
    mock_isdir.return_value = True
    mock_loader.return_value = "   "
    mock_site_path.return_value = "some/path"

    root_names = {"Title": "name"}
    result = gen_api(root_names, prefix="test_docs")

    mock_isdir.assert_called_once_with("test_docs")
    mock_mkdir.assert_not_called()
    mock_write.assert_not_called()
    assert len(result) == 0

def test_gen_api_with_pwd(mock_logger, mock_isdir, mock_mkdir, mock_loader, mock_site_path, mock_write, mock_sys_path):
    mock_isdir.return_value = True
    mock_loader.return_value = "some documentation"
    mock_site_path.return_value = "some/path"

    root_names = {"Title": "name"}
    pwd = "some/pwd"
    result = gen_api(root_names, pwd=pwd, prefix="test_docs")

    assert pwd in mock_sys_path
    mock_isdir.assert_called_once_with("test_docs")
    mock_mkdir.assert_not_called()
    assert len(result) == 1
    assert "some documentation" in result[0]
