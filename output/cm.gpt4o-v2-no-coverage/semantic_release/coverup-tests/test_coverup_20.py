# file: semantic_release/hvcs.py:455-466
# asked: {"lines": [455, 465, 466], "branches": []}
# gained: {"lines": [455, 465, 466], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import post_changelog

@pytest.fixture
def mock_get_hvcs():
    with patch('semantic_release.hvcs.get_hvcs') as mock:
        yield mock

def test_post_changelog_success(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.post_release_changelog.return_value = True
    mock_get_hvcs.return_value = mock_hvcs_instance

    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release."

    result = post_changelog(owner, repository, version, changelog)

    mock_get_hvcs.assert_called_once()
    mock_hvcs_instance.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is True

def test_post_changelog_failure(mock_get_hvcs):
    mock_hvcs_instance = MagicMock()
    mock_hvcs_instance.post_release_changelog.return_value = False
    mock_get_hvcs.return_value = mock_hvcs_instance

    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release."

    result = post_changelog(owner, repository, version, changelog)

    mock_get_hvcs.assert_called_once()
    mock_hvcs_instance.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is False
