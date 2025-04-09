# file: semantic_release/hvcs.py:198-219
# asked: {"lines": [211, 212, 213, 215, 216, 217, 218, 219], "branches": [[217, 218], [217, 219]]}
# gained: {"lines": [211, 212, 213, 215, 216, 217, 218, 219], "branches": [[217, 218], [217, 219]]}

import pytest
from unittest.mock import patch, Mock
from requests import HTTPError
from semantic_release.hvcs import Github

@pytest.fixture
def mock_github_session(monkeypatch):
    mock_session = Mock()
    monkeypatch.setattr(Github, 'session', lambda: mock_session)
    return mock_session

def test_get_release_success(mock_github_session):
    mock_response = Mock()
    mock_response.json.return_value = {"id": 123}
    mock_github_session.get.return_value = mock_response

    release_id = Github.get_release("owner", "repo", "tag")
    assert release_id == 123

def test_get_release_not_found(mock_github_session):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = HTTPError(response=Mock(status_code=404))
    mock_github_session.get.side_effect = HTTPError(response=Mock(status_code=404))

    release_id = Github.get_release("owner", "repo", "tag")
    assert release_id is None

def test_get_release_http_error(mock_github_session, caplog):
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = HTTPError(response=Mock(status_code=500))
    mock_github_session.get.side_effect = HTTPError(response=Mock(status_code=500))

    with caplog.at_level('DEBUG'):
        release_id = Github.get_release("owner", "repo", "tag")
        assert release_id is None
        assert "Get release by tag on Github has failed" in caplog.text
