# file semantic_release/hvcs.py:198-219
# lines [198, 199, 200, 211, 212, 213, 215, 216, 217, 218, 219]
# branches ['217->218', '217->219']

import pytest
import requests
from requests.exceptions import HTTPError
from unittest.mock import patch, Mock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock_session = mocker.patch('semantic_release.hvcs.Github.session', autospec=True)
    return mock_session

def test_github_get_release_success(mock_github_session):
    mock_response = Mock()
    mock_response.json.return_value = {"id": 123}
    mock_github_session.return_value.get.return_value = mock_response

    release_id = Github.get_release("owner", "repo", "tag")
    assert release_id == 123

def test_github_get_release_not_found(mock_github_session):
    mock_response = Mock()
    mock_response.json.return_value = {}
    mock_github_session.return_value.get.return_value = mock_response

    release_id = Github.get_release("owner", "repo", "tag")
    assert release_id is None

def test_github_get_release_http_error(mock_github_session):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = HTTPError(response=Mock(status_code=500))
    mock_github_session.return_value.get.side_effect = HTTPError(response=mock_response)

    release_id = Github.get_release("owner", "repo", "tag")
    assert release_id is None
