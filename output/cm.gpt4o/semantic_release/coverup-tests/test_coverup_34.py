# file semantic_release/hvcs.py:316-342
# lines [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342]
# branches ['330->331', '330->335', '336->337', '336->342', '339->336', '339->340']

import os
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_os_listdir(mocker):
    return mocker.patch('os.listdir')

@pytest.fixture
def mock_os_path_join(mocker):
    return mocker.patch('os.path.join', side_effect=lambda *args: "/".join(args))

@pytest.fixture
def mock_get_release(mocker):
    return mocker.patch('semantic_release.hvcs.Github.get_release')

@pytest.fixture
def mock_upload_asset(mocker):
    return mocker.patch('semantic_release.hvcs.Github.upload_asset')

def test_upload_dists_no_release_found(mock_get_release, mock_os_listdir, mock_os_path_join, mock_upload_asset):
    mock_get_release.return_value = None
    result = Github.upload_dists('owner', 'repo', '1.0.0', 'path')
    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_os_listdir.assert_not_called()
    mock_os_path_join.assert_not_called()
    mock_upload_asset.assert_not_called()

def test_upload_dists_assets_uploaded_successfully(mock_get_release, mock_os_listdir, mock_os_path_join, mock_upload_asset):
    mock_get_release.return_value = 'release_id'
    mock_os_listdir.return_value = ['file1', 'file2']
    mock_upload_asset.return_value = True

    result = Github.upload_dists('owner', 'repo', '1.0.0', 'path')
    assert result is True
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_os_listdir.assert_called_once_with('path')
    mock_os_path_join.assert_any_call('path', 'file1')
    mock_os_path_join.assert_any_call('path', 'file2')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file1')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file2')

def test_upload_dists_one_or_more_assets_failed(mock_get_release, mock_os_listdir, mock_os_path_join, mock_upload_asset):
    mock_get_release.return_value = 'release_id'
    mock_os_listdir.return_value = ['file1', 'file2']
    mock_upload_asset.side_effect = [True, False]

    result = Github.upload_dists('owner', 'repo', '1.0.0', 'path')
    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_os_listdir.assert_called_once_with('path')
    mock_os_path_join.assert_any_call('path', 'file1')
    mock_os_path_join.assert_any_call('path', 'file2')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file1')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file2')
