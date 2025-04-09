# file semantic_release/hvcs.py:198-219
# lines [198, 199, 200, 211, 212, 213, 215, 216, 217, 218, 219]
# branches ['217->218', '217->219']

import pytest
from unittest.mock import MagicMock, patch
from requests.exceptions import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock = mocker.patch('semantic_release.hvcs.Github.session', autospec=True)
    mock.return_value.get.return_value.json.return_value = {"id": 123}
    return mock

@pytest.fixture
def mock_response(mocker):
    mock = MagicMock()
    mock.status_code = 404
    return mock

def test_get_release_success(mock_github_session):
    owner = "owner"
    repo = "repo"
    tag = "v1.0.0"
    release_id = Github.get_release(owner, repo, tag)
    assert release_id == 123
    mock_github_session.return_value.get.assert_called_once_with(
        f"https://api.github.com/repos/{owner}/{repo}/releases/tags/{tag}"
    )

def test_get_release_http_error_not_404(mocker, mock_github_session, mock_response):
    mock_github_session.return_value.get.side_effect = HTTPError(response=mock_response)
    mock_logger_debug = mocker.patch('semantic_release.hvcs.logger.debug')
    owner = "owner"
    repo = "repo"
    tag = "v1.0.0"
    mock_response.status_code = 500  # Simulate an HTTP error other than 404
    with patch('semantic_release.hvcs.logger') as mock_logger:
        release_id = Github.get_release(owner, repo, tag)
        assert release_id is None
        mock_logger.debug.assert_called_once_with(f"Get release by tag on Github has failed: {mock_github_session.return_value.get.side_effect}")

def test_get_release_http_error_404(mock_github_session, mock_response):
    mock_github_session.return_value.get.side_effect = HTTPError(response=mock_response)
    owner = "owner"
    repo = "repo"
    tag = "v1.0.0"
    release_id = Github.get_release(owner, repo, tag)
    assert release_id is None
