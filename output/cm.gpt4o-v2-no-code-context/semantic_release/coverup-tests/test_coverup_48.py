# file: semantic_release/hvcs.py:373-397
# asked: {"lines": [], "branches": [[394, 387]]}
# gained: {"lines": [], "branches": [[394, 387]]}

import pytest
from unittest.mock import MagicMock, patch
from semantic_release.hvcs import Gitlab

@pytest.fixture
def mock_gitlab(mocker):
    mock_gitlab_instance = mocker.patch('semantic_release.hvcs.gitlab')
    mock_gitlab_instance.Gitlab.api_url.return_value = 'https://gitlab.com/api/v4'
    mock_gitlab_instance.Gitlab.token.return_value = 'fake_token'
    return mock_gitlab_instance

def test_check_build_status_success(mock_gitlab):
    mock_gitlab_instance = mock_gitlab.Gitlab.return_value
    mock_gitlab_instance.auth.return_value = None
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [
        {"status": "success", "name": "job1"},
        {"status": "skipped", "name": "job2"}
    ]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is True

def test_check_build_status_pending(mock_gitlab, caplog):
    mock_gitlab_instance = mock_gitlab.Gitlab.return_value
    mock_gitlab_instance.auth.return_value = None
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [
        {"status": "pending", "name": "job1"}
    ]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    with caplog.at_level('DEBUG'):
        result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is False
    assert "check_build_status: job job1 is still in pending status" in caplog.text

def test_check_build_status_failed(mock_gitlab, caplog):
    mock_gitlab_instance = mock_gitlab.Gitlab.return_value
    mock_gitlab_instance.auth.return_value = None
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [
        {"status": "failed", "name": "job1", "allow_failure": False}
    ]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    with caplog.at_level('DEBUG'):
        result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is False
    assert "check_build_status: job job1 failed" in caplog.text

def test_check_build_status_failed_allow_failure(mock_gitlab):
    mock_gitlab_instance = mock_gitlab.Gitlab.return_value
    mock_gitlab_instance.auth.return_value = None
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [
        {"status": "failed", "name": "job1", "allow_failure": True}
    ]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is True
