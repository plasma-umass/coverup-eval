# file semantic_release/hvcs.py:316-342
# lines [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342]
# branches ['330->331', '330->335', '336->337', '336->342', '339->336', '339->340']

import os
from unittest.mock import patch
import pytest
from semantic_release.hvcs import Github

@pytest.fixture
def mock_os_listdir(mocker):
    return mocker.patch('os.listdir', return_value=['file1.txt', 'file2.txt'])

@pytest.fixture
def mock_os_path_join(mocker):
    return mocker.patch('os.path.join', side_effect=lambda p, f: f"{p}/{f}")

@pytest.fixture
def mock_get_release(mocker):
    return mocker.patch.object(Github, 'get_release', return_value=1)

@pytest.fixture
def mock_upload_asset_success(mocker):
    return mocker.patch.object(Github, 'upload_asset', return_value=True)

@pytest.fixture
def mock_upload_asset_failure(mocker):
    return mocker.patch.object(Github, 'upload_asset', side_effect=[True, False])

def test_upload_dists_success(mock_os_listdir, mock_os_path_join, mock_get_release, mock_upload_asset_success):
    assert Github.upload_dists('owner', 'repo', '1.0.0', 'dist_path') is True
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    assert mock_upload_asset_success.call_count == 2

def test_upload_dists_failure(mock_os_listdir, mock_os_path_join, mock_get_release, mock_upload_asset_failure):
    assert Github.upload_dists('owner', 'repo', '1.0.0', 'dist_path') is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    assert mock_upload_asset_failure.call_count == 2

def test_upload_dists_no_release(mock_os_listdir, mock_os_path_join, mocker):
    mocker.patch.object(Github, 'get_release', return_value=None)
    assert Github.upload_dists('owner', 'repo', '1.0.0', 'dist_path') is False
