# file semantic_release/hvcs.py:373-397
# lines [384, 385, 386, 387, 388, 389, 390, 391, 393, 394, 395, 396, 397]
# branches ['387->388', '387->397', '388->387', '388->389', '389->390', '389->394', '394->387', '394->395']

import pytest
from unittest.mock import MagicMock
from semantic_release.hvcs import Gitlab

@pytest.fixture
def mock_gitlab(mocker):
    mocker.patch('semantic_release.hvcs.gitlab')
    gl_mock = mocker.MagicMock()
    mocker.patch('semantic_release.hvcs.Gitlab.api_url', return_value='https://gitlab.com/api/v4')
    mocker.patch('semantic_release.hvcs.Gitlab.token', return_value='token')
    mocker.patch('semantic_release.hvcs.gitlab.Gitlab', return_value=gl_mock)
    return gl_mock

def test_check_build_status_pending(mock_gitlab):
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_gitlab.projects.get.return_value = mock_project
    mock_project.commits.get.return_value = mock_commit
    mock_commit.statuses.list.return_value = [
        {'name': 'test_job', 'status': 'pending'}
    ]

    assert not Gitlab.check_build_status('owner', 'repo', 'ref')
    mock_gitlab.projects.get.assert_called_once_with('owner/repo')
    mock_project.commits.get.assert_called_once_with('ref')
    mock_commit.statuses.list.assert_called_once()

def test_check_build_status_failed(mock_gitlab):
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_gitlab.projects.get.return_value = mock_project
    mock_project.commits.get.return_value = mock_commit
    mock_commit.statuses.list.return_value = [
        {'name': 'test_job', 'status': 'failed', 'allow_failure': False}
    ]

    assert not Gitlab.check_build_status('owner', 'repo', 'ref')
    mock_gitlab.projects.get.assert_called_once_with('owner/repo')
    mock_project.commits.get.assert_called_once_with('ref')
    mock_commit.statuses.list.assert_called_once()

def test_check_build_status_success(mock_gitlab):
    mock_project = MagicMock()
    mock_commit = MagicMock()
    mock_gitlab.projects.get.return_value = mock_project
    mock_project.commits.get.return_value = mock_commit
    mock_commit.statuses.list.return_value = [
        {'name': 'test_job', 'status': 'success'}
    ]

    assert Gitlab.check_build_status('owner', 'repo', 'ref')
    mock_gitlab.projects.get.assert_called_once_with('owner/repo')
    mock_project.commits.get.assert_called_once_with('ref')
    mock_commit.statuses.list.assert_called_once()
