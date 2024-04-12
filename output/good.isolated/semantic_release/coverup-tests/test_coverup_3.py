# file semantic_release/hvcs.py:469-481
# lines [469, 481]
# branches []

import pytest
from unittest.mock import MagicMock
from semantic_release.hvcs import get_hvcs, upload_to_release

@pytest.fixture
def mock_hvcs(mocker):
    hvcs_mock = MagicMock()
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=hvcs_mock)
    return hvcs_mock

def test_upload_to_release(mock_hvcs):
    owner = 'test_owner'
    repository = 'test_repo'
    version = '1.0.0'
    path = 'dist'

    mock_hvcs.upload_dists.return_value = True

    assert upload_to_release(owner, repository, version, path) == True
    mock_hvcs.upload_dists.assert_called_once_with(owner, repository, version, path)
