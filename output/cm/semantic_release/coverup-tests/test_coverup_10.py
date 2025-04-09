# file semantic_release/hvcs.py:455-466
# lines [455, 465, 466]
# branches []

import pytest
from unittest.mock import MagicMock
from semantic_release.hvcs import post_changelog, get_hvcs

@pytest.fixture
def mock_hvcs(mocker):
    mock = MagicMock()
    mocker.patch('semantic_release.hvcs.get_hvcs', return_value=mock)
    return mock

def test_post_changelog(mock_hvcs):
    owner = 'test_owner'
    repository = 'test_repo'
    version = '1.0.0'
    changelog = 'New features and bug fixes'

    success = post_changelog(owner, repository, version, changelog)

    mock_hvcs.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert success == mock_hvcs.post_release_changelog.return_value
