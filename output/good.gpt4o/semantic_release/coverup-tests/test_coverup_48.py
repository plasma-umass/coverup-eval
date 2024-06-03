# file semantic_release/hvcs.py:373-397
# lines [384, 385, 386, 387, 388, 389, 390, 391, 393, 394, 395, 396, 397]
# branches ['387->388', '387->397', '388->387', '388->389', '389->390', '389->394', '394->387', '394->395']

import pytest
from unittest.mock import patch, MagicMock
from semantic_release.hvcs import Gitlab

@pytest.fixture
def mock_gitlab(mocker):
    mock_gitlab_instance = mocker.patch('semantic_release.hvcs.gitlab')
    mock_gitlab_instance.Gitlab.return_value.auth.return_value = None
    return mock_gitlab_instance

def test_check_build_status_pending(mocker, mock_gitlab):
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [{"status": "pending", "name": "test_job"}]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab.Gitlab.return_value.projects.get.return_value = mock_project

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is False

def test_check_build_status_failed(mocker, mock_gitlab):
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [{"status": "failed", "name": "test_job", "allow_failure": False}]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab.Gitlab.return_value.projects.get.return_value = mock_project

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is False

def test_check_build_status_success(mocker, mock_gitlab):
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [{"status": "success", "name": "test_job"}]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab.Gitlab.return_value.projects.get.return_value = mock_project

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is True

def test_check_build_status_skipped(mocker, mock_gitlab):
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_status = MagicMock()
    mock_status.list.return_value = [{"status": "skipped", "name": "test_job"}]
    mock_commit.statuses = mock_status
    mock_project.commits.get.return_value = mock_commit
    mock_gitlab.Gitlab.return_value.projects.get.return_value = mock_project

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is True
