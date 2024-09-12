# file: semantic_release/hvcs.py:316-342
# asked: {"lines": [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342], "branches": [[330, 331], [330, 335], [336, 337], [336, 342], [339, 336], [339, 340]]}
# gained: {"lines": [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342], "branches": [[330, 331], [330, 335], [336, 337], [336, 342], [339, 336], [339, 340]]}

import os
import pytest
from unittest.mock import patch, MagicMock

from semantic_release.hvcs import Github

@pytest.fixture
def mock_get_release(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(Github, 'get_release', mock)
    return mock

@pytest.fixture
def mock_upload_asset(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(Github, 'upload_asset', mock)
    return mock

@pytest.fixture
def mock_listdir(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(os, 'listdir', mock)
    return mock

@pytest.fixture
def mock_path_join(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr(os.path, 'join', mock)
    return mock

def test_upload_dists_no_release_found(mock_get_release):
    mock_get_release.return_value = None
    result = Github.upload_dists('owner', 'repo', '1.0.0', 'path')
    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')

def test_upload_dists_all_assets_uploaded(mock_get_release, mock_upload_asset, mock_listdir, mock_path_join):
    mock_get_release.return_value = 'release_id'
    mock_listdir.return_value = ['file1', 'file2']
    mock_path_join.side_effect = lambda path, file: f'{path}/{file}'
    mock_upload_asset.return_value = True

    result = Github.upload_dists('owner', 'repo', '1.0.0', 'path')
    assert result is True
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_listdir.assert_called_once_with('path')
    mock_path_join.assert_any_call('path', 'file1')
    mock_path_join.assert_any_call('path', 'file2')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file1')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file2')

def test_upload_dists_some_assets_failed(mock_get_release, mock_upload_asset, mock_listdir, mock_path_join):
    mock_get_release.return_value = 'release_id'
    mock_listdir.return_value = ['file1', 'file2']
    mock_path_join.side_effect = lambda path, file: f'{path}/{file}'
    mock_upload_asset.side_effect = [True, False]

    result = Github.upload_dists('owner', 'repo', '1.0.0', 'path')
    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_listdir.assert_called_once_with('path')
    mock_path_join.assert_any_call('path', 'file1')
    mock_path_join.assert_any_call('path', 'file2')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file1')
    mock_upload_asset.assert_any_call('owner', 'repo', 'release_id', 'path/file2')
