# file semantic_release/hvcs.py:198-219
# lines []
# branches ['217->219']

import pytest
from unittest.mock import patch, Mock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(mocker):
    mock_session = mocker.patch('semantic_release.hvcs.Github.session')
    return mock_session

def test_github_get_release_handles_non_404_http_error(mock_github_session):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_response.json.return_value = {}
    
    mock_session_instance = Mock()
    mock_session_instance.get.side_effect = HTTPError(response=mock_response)
    mock_github_session.return_value = mock_session_instance

    with patch('semantic_release.hvcs.logger') as mock_logger:
        result = Github.get_release('owner', 'repo', 'tag')
        assert result is None
        mock_logger.debug.assert_called_once_with("Get release by tag on Github has failed: ")

def test_github_get_release_handles_404_http_error(mock_github_session):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.json.return_value = {}
    
    mock_session_instance = Mock()
    mock_session_instance.get.side_effect = HTTPError(response=mock_response)
    mock_github_session.return_value = mock_session_instance

    with patch('semantic_release.hvcs.logger') as mock_logger:
        result = Github.get_release('owner', 'repo', 'tag')
        assert result is None
        mock_logger.debug.assert_not_called()
