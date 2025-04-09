# file: semantic_release/hvcs.py:198-219
# asked: {"lines": [198, 199, 200, 211, 212, 213, 215, 216, 217, 218, 219], "branches": [[217, 218], [217, 219]]}
# gained: {"lines": [198, 199, 200, 211, 212, 213, 215, 216, 217, 218, 219], "branches": [[217, 218], [217, 219]]}

import pytest
from requests import HTTPError
from unittest.mock import patch, Mock
from semantic_release.hvcs import Github

@pytest.fixture
def mock_logger(mocker):
    return mocker.patch('semantic_release.hvcs.logger')

@pytest.fixture
def mock_session(mocker):
    return mocker.patch('semantic_release.hvcs.Github.session')

def test_get_release_success(mock_session):
    mock_response = Mock()
    mock_response.json.return_value = {"id": 123}
    mock_session.return_value.get.return_value = mock_response

    result = Github.get_release("owner", "repo", "tag")
    assert result == 123

def test_get_release_not_found(mock_session):
    mock_session.return_value.get.side_effect = HTTPError(response=Mock(status_code=404))

    result = Github.get_release("owner", "repo", "tag")
    assert result is None

def test_get_release_other_http_error(mock_session, mock_logger):
    mock_session.return_value.get.side_effect = HTTPError(response=Mock(status_code=500))

    result = Github.get_release("owner", "repo", "tag")
    assert result is None
    mock_logger.debug.assert_called_once_with("Get release by tag on Github has failed: ")

