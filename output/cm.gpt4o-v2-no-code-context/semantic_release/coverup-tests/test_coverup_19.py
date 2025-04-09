# file: semantic_release/hvcs.py:469-481
# asked: {"lines": [469, 481], "branches": []}
# gained: {"lines": [469, 481], "branches": []}

import pytest
from unittest.mock import Mock, patch
from semantic_release.hvcs import upload_to_release, get_hvcs

@pytest.fixture
def mock_get_hvcs(monkeypatch):
    mock_hvcs = Mock()
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: mock_hvcs)
    return mock_hvcs

def test_upload_to_release_success(mock_get_hvcs):
    mock_get_hvcs.upload_dists.return_value = True

    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    path = "dist/"

    result = upload_to_release(owner, repository, version, path)

    mock_get_hvcs.upload_dists.assert_called_once_with(owner, repository, version, path)
    assert result is True

def test_upload_to_release_failure(mock_get_hvcs):
    mock_get_hvcs.upload_dists.return_value = False

    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    path = "dist/"

    result = upload_to_release(owner, repository, version, path)

    mock_get_hvcs.upload_dists.assert_called_once_with(owner, repository, version, path)
    assert result is False
