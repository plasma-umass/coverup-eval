# file: semantic_release/hvcs.py:469-481
# asked: {"lines": [481], "branches": []}
# gained: {"lines": [481], "branches": []}

import pytest
from unittest.mock import Mock, patch
from semantic_release.hvcs import upload_to_release

@pytest.fixture
def mock_get_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock:
        yield mock

def test_upload_to_release(mock_get_hvcs):
    mock_hvcs_instance = Mock()
    mock_get_hvcs.return_value = mock_hvcs_instance
    mock_hvcs_instance.upload_dists.return_value = True

    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    path = "/fake/path"

    result = upload_to_release(owner, repository, version, path)

    mock_get_hvcs.assert_called_once()
    mock_hvcs_instance.upload_dists.assert_called_once_with(owner, repository, version, path)
    assert result is True
