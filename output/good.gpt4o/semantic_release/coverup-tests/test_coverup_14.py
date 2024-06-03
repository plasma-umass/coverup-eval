# file semantic_release/hvcs.py:137-143
# lines [137, 138, 139, 141, 142, 143]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from requests import Session
from semantic_release.hvcs import Github, build_requests_session

@pytest.fixture
def mock_build_requests_session(mocker):
    return mocker.patch('semantic_release.hvcs.build_requests_session')

@pytest.fixture
def mock_github_auth(mocker):
    return mocker.patch('semantic_release.hvcs.Github.auth')

def test_github_session(mock_build_requests_session, mock_github_auth):
    # Arrange
    mock_session = MagicMock(spec=Session)
    mock_build_requests_session.return_value = mock_session
    mock_auth = ('user', 'token')
    mock_github_auth.return_value = mock_auth

    # Act
    session = Github.session()

    # Assert
    mock_build_requests_session.assert_called_once_with(raise_for_status=True, retry=True)
    assert session.auth == mock_auth
    assert session == mock_session
