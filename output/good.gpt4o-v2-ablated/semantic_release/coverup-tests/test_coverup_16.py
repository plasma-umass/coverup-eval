# file: semantic_release/hvcs.py:455-466
# asked: {"lines": [455, 465, 466], "branches": []}
# gained: {"lines": [455, 465, 466], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from semantic_release.hvcs import post_changelog

@pytest.fixture
def mock_get_hvcs(monkeypatch):
    mock_hvcs = MagicMock()
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: mock_hvcs)
    return mock_hvcs

def test_post_changelog_success(mock_get_hvcs):
    mock_get_hvcs.post_release_changelog.return_value = True
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release"

    result = post_changelog(owner, repository, version, changelog)

    mock_get_hvcs.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is True

def test_post_changelog_failure(mock_get_hvcs):
    mock_get_hvcs.post_release_changelog.return_value = False
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release"

    result = post_changelog(owner, repository, version, changelog)

    mock_get_hvcs.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is False
