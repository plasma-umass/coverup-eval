# file semantic_release/hvcs.py:168-196
# lines [168, 169, 170, 182, 183, 184, 185, 186, 187, 188, 189, 190, 193, 194, 195, 196]
# branches []

import pytest
from unittest.mock import Mock
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github, logger

@pytest.fixture
def mock_github_session(mocker):
    mock = mocker.patch('semantic_release.hvcs.Github.session')
    mock.return_value.post = Mock()
    return mock.return_value

def test_github_create_release_success(mock_github_session):
    owner = 'owner'
    repo = 'repo'
    tag = 'v1.0.0'
    changelog = 'New features'

    assert Github.create_release(owner, repo, tag, changelog) is True
    mock_github_session.post.assert_called_once_with(
        f"{Github.api_url()}/repos/{owner}/{repo}/releases",
        json={
            "tag_name": tag,
            "name": tag,
            "body": changelog,
            "draft": False,
            "prerelease": False,
        },
    )

def test_github_create_release_failure(mock_github_session, mocker):
    owner = 'owner'
    repo = 'repo'
    tag = 'v1.0.0'
    changelog = 'New features'
    mock_github_session.post.side_effect = HTTPError("Error")

    mocker.patch.object(logger, 'warning')

    assert Github.create_release(owner, repo, tag, changelog) is False
    logger.warning.assert_called_once()
    assert "Release creation on Github has failed" in logger.warning.call_args[0][0]
