# file: semantic_release/hvcs.py:316-342
# asked: {"lines": [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342], "branches": [[330, 331], [330, 335], [336, 337], [336, 342], [339, 336], [339, 340]]}
# gained: {"lines": [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342], "branches": [[330, 331], [330, 335], [336, 337], [336, 342], [339, 336], [339, 340]]}

import os
import pytest
from unittest.mock import patch, mock_open

from semantic_release.hvcs import Github

@pytest.fixture
def mock_get_release():
    with patch('semantic_release.hvcs.Github.get_release') as mock:
        yield mock

@pytest.fixture
def mock_upload_asset():
    with patch('semantic_release.hvcs.Github.upload_asset') as mock:
        yield mock

@pytest.fixture
def mock_os_listdir():
    with patch('os.listdir') as mock:
        yield mock

@pytest.fixture
def mock_os_path_join():
    with patch('os.path.join', side_effect=lambda *args: "/".join(args)) as mock:
        yield mock

@pytest.fixture
def mock_open_file():
    with patch('builtins.open', mock_open(read_data="data")) as mock:
        yield mock

def test_upload_dists_success(mock_get_release, mock_upload_asset, mock_os_listdir, mock_os_path_join, mock_open_file):
    mock_get_release.return_value = 123
    mock_upload_asset.return_value = True
    mock_os_listdir.return_value = ['file1', 'file2']

    result = Github.upload_dists('owner', 'repo', '1.0.0', '/path/to/dist')

    assert result is True
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    assert mock_upload_asset.call_count == 2

def test_upload_dists_no_release(mock_get_release, mock_upload_asset, mock_os_listdir, mock_os_path_join, mock_open_file):
    mock_get_release.return_value = None

    result = Github.upload_dists('owner', 'repo', '1.0.0', '/path/to/dist')

    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_upload_asset.assert_not_called()

def test_upload_dists_partial_failure(mock_get_release, mock_upload_asset, mock_os_listdir, mock_os_path_join, mock_open_file):
    mock_get_release.return_value = 123
    mock_upload_asset.side_effect = [True, False]
    mock_os_listdir.return_value = ['file1', 'file2']

    result = Github.upload_dists('owner', 'repo', '1.0.0', '/path/to/dist')

    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    assert mock_upload_asset.call_count == 2
