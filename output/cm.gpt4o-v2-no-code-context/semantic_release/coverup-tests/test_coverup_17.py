# file: semantic_release/hvcs.py:455-466
# asked: {"lines": [455, 465, 466], "branches": []}
# gained: {"lines": [455, 465, 466], "branches": []}

import pytest
from unittest.mock import MagicMock, patch
from semantic_release.hvcs import post_changelog, get_hvcs

@pytest.fixture
def mock_hvcs(monkeypatch):
    mock = MagicMock()
    monkeypatch.setattr('semantic_release.hvcs.get_hvcs', lambda: mock)
    return mock

def test_post_changelog_success(mock_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release"

    mock_hvcs.post_release_changelog.return_value = True

    result = post_changelog(owner, repository, version, changelog)

    mock_hvcs.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is True

def test_post_changelog_failure(mock_hvcs):
    owner = "test_owner"
    repository = "test_repo"
    version = "1.0.0"
    changelog = "Initial release"

    mock_hvcs.post_release_changelog.return_value = False

    result = post_changelog(owner, repository, version, changelog)

    mock_hvcs.post_release_changelog.assert_called_once_with(owner, repository, version, changelog)
    assert result is False
