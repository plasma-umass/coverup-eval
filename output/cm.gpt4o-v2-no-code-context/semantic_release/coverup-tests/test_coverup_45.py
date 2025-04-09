# file: semantic_release/hvcs.py:373-397
# asked: {"lines": [384, 385, 386, 387, 388, 389, 390, 391, 393, 394, 395, 396, 397], "branches": [[387, 388], [387, 397], [388, 387], [388, 389], [389, 390], [389, 394], [394, 387], [394, 395]]}
# gained: {"lines": [384, 385, 386, 387, 388, 389, 390, 391, 393, 394, 395, 396, 397], "branches": [[387, 388], [387, 397], [388, 387], [388, 389], [389, 390], [389, 394], [394, 395]]}

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
    mock_statuses = MagicMock()
    mock_statuses.list.return_value = [{"status": "success"}]
    mock_commit.statuses = mock_statuses
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is True

def test_check_build_status_pending(mock_gitlab):
    mock_gitlab_instance = mock_gitlab.Gitlab.return_value
    mock_gitlab_instance.auth.return_value = None
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_statuses = MagicMock()
    mock_statuses.list.return_value = [{"status": "pending", "name": "job1"}]
    mock_commit.statuses = mock_statuses
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is False

def test_check_build_status_failed(mock_gitlab):
    mock_gitlab_instance = mock_gitlab.Gitlab.return_value
    mock_gitlab_instance.auth.return_value = None
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_statuses = MagicMock()
    mock_statuses.list.return_value = [{"status": "failed", "allow_failure": False, "name": "job1"}]
    mock_commit.statuses = mock_statuses
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is False

def test_check_build_status_skipped(mock_gitlab):
    mock_gitlab_instance = mock_gitlab.Gitlab.return_value
    mock_gitlab_instance.auth.return_value = None
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_statuses = MagicMock()
    mock_statuses.list.return_value = [{"status": "skipped"}]
    mock_commit.statuses = mock_statuses
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab_instance.projects.get.return_value = mock_project

    result = Gitlab.check_build_status('owner', 'repo', 'ref')
    assert result is True
