# file: semantic_release/hvcs.py:316-342
# asked: {"lines": [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342], "branches": [[330, 331], [330, 335], [336, 337], [336, 342], [339, 336], [339, 340]]}
# gained: {"lines": [316, 317, 329, 330, 331, 332, 335, 336, 337, 339, 340, 342], "branches": [[330, 331], [330, 335], [336, 337], [336, 342], [339, 336], [339, 340]]}

import os
import pytest
from unittest.mock import patch, MagicMock

from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_methods(monkeypatch):
    mock_get_release = MagicMock()
    mock_upload_asset = MagicMock()
    monkeypatch.setattr(Github, 'get_release', mock_get_release)
    monkeypatch.setattr(Github, 'upload_asset', mock_upload_asset)
    return mock_get_release, mock_upload_asset

def test_upload_dists_no_release_found(mock_github_methods):
    mock_get_release, mock_upload_asset = mock_github_methods
    mock_get_release.return_value = None

    result = Github.upload_dists('owner', 'repo', '1.0.0', 'path')

    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    mock_upload_asset.assert_not_called()

def test_upload_dists_all_assets_uploaded_successfully(mock_github_methods, tmpdir):
    mock_get_release, mock_upload_asset = mock_github_methods
    mock_get_release.return_value = 'release_id'
    mock_upload_asset.return_value = True

    # Create dummy files in the temporary directory
    tmpdir.join('file1.txt').write('content1')
    tmpdir.join('file2.txt').write('content2')

    result = Github.upload_dists('owner', 'repo', '1.0.0', str(tmpdir))

    assert result is True
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    assert mock_upload_asset.call_count == 2

def test_upload_dists_one_or_more_assets_failed(mock_github_methods, tmpdir):
    mock_get_release, mock_upload_asset = mock_github_methods
    mock_get_release.return_value = 'release_id'
    mock_upload_asset.side_effect = [True, False]

    # Create dummy files in the temporary directory
    tmpdir.join('file1.txt').write('content1')
    tmpdir.join('file2.txt').write('content2')

    result = Github.upload_dists('owner', 'repo', '1.0.0', str(tmpdir))

    assert result is False
    mock_get_release.assert_called_once_with('owner', 'repo', 'v1.0.0')
    assert mock_upload_asset.call_count == 2
