# file semantic_release/hvcs.py:455-466
# lines [455, 465, 466]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import post_changelog

@pytest.fixture
def mock_get_hvcs(mocker):
    mock_hvcs = mocker.patch('semantic_release.hvcs.get_hvcs')
    mock_instance = MagicMock()
    mock_hvcs.return_value = mock_instance
    return mock_instance

def test_post_changelog_success(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release"

    mock_get_hvcs.post_release_changelog.return_value = True

    result = post_changelog(owner, repository, version, changelog)

    mock_get_hvcs.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is True

def test_post_changelog_failure(mock_get_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release"

    mock_get_hvcs.post_release_changelog.return_value = False

    result = post_changelog(owner, repository, version, changelog)

    mock_get_hvcs.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is False
