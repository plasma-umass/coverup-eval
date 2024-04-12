# file semantic_release/hvcs.py:221-243
# lines [221, 222, 223, 235, 236, 237, 238, 240, 241, 242, 243]
# branches []

import pytest
from unittest.mock import patch
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock = mocker.patch('semantic_release.hvcs.Github.session')
    mock.return_value.post.return_value = mocker.Mock()
    return mock.return_value

def test_edit_release_success(mock_github_session):
    owner = "test_owner"
    repo = "test_repo"
    id = 123
    changelog = "Test changelog"

    assert Github.edit_release(owner, repo, id, changelog) is True
    mock_github_session.post.assert_called_once_with(
        f"https://api.github.com/repos/{owner}/{repo}/releases/{id}",
        json={"body": changelog},
    )

def test_edit_release_failure(mock_github_session, mocker):
    owner = "test_owner"
    repo = "test_repo"
    id = 123
    changelog = "Test changelog"
    mock_github_session.post.side_effect = HTTPError("404 Client Error: Not Found for url")

    with patch('semantic_release.hvcs.logger') as mock_logger:
        assert Github.edit_release(owner, repo, id, changelog) is False
        mock_logger.warning.assert_called_once()
