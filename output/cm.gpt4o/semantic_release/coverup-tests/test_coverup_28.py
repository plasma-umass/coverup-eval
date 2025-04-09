# file semantic_release/hvcs.py:469-481
# lines [469, 481]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import upload_to_release

@pytest.fixture
def mock_get_hvcs(mocker):
    mock_hvcs = mocker.patch('semantic_release.hvcs.get_hvcs')
    mock_instance = MagicMock()
    mock_hvcs.return_value = mock_instance
    return mock_instance

def test_upload_to_release_success(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    path = "dist/"

    mock_get_hvcs.upload_dists.return_value = True

    result = upload_to_release(owner, repository, version, path)

    mock_get_hvcs.upload_dists.assert_called_once_with(owner, repository, version, path)
    assert result is True

def test_upload_to_release_failure(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    path = "dist/"

    mock_get_hvcs.upload_dists.return_value = False

    result = upload_to_release(owner, repository, version, path)

    mock_get_hvcs.upload_dists.assert_called_once_with(owner, repository, version, path)
    assert result is False
