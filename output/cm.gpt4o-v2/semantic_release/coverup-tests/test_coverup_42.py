# file: semantic_release/hvcs.py:373-397
# asked: {"lines": [384, 385, 386, 387, 388, 389, 390, 391, 393, 394, 395, 396, 397], "branches": [[387, 388], [387, 397], [388, 387], [388, 389], [389, 390], [389, 394], [394, 387], [394, 395]]}
# gained: {"lines": [384, 385, 386, 387, 388, 389, 390, 391, 393, 394, 395, 396, 397], "branches": [[387, 388], [387, 397], [388, 387], [388, 389], [389, 390], [389, 394], [394, 387], [394, 395]]}

import pytest
from unittest.mock import MagicMock, patch
from semantic_release.hvcs import Gitlab

@pytest.fixture
def mock_gitlab():
    with patch('semantic_release.hvcs.gitlab') as mock:
        yield mock

@pytest.fixture
def mock_logger():
    with patch('semantic_release.hvcs.logger') as mock:
        yield mock

def test_check_build_status_success(mock_gitlab, mock_logger):
    mock_instance = mock_gitlab.Gitlab.return_value
    mock_instance.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [
        {"status": "success", "name": "job1"},
        {"status": "skipped", "name": "job2"}
    ]

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is True

def test_check_build_status_pending(mock_gitlab, mock_logger):
    mock_instance = mock_gitlab.Gitlab.return_value
    mock_instance.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [
        {"status": "pending", "name": "job1"}
    ]

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is False
    mock_logger.debug.assert_called_with("check_build_status: job job1 is still in pending status")

def test_check_build_status_failed(mock_gitlab, mock_logger):
    mock_instance = mock_gitlab.Gitlab.return_value
    mock_instance.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [
        {"status": "failed", "name": "job1", "allow_failure": False}
    ]

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is False
    mock_logger.debug.assert_called_with("check_build_status: job job1 failed")

def test_check_build_status_failed_but_allowed(mock_gitlab, mock_logger):
    mock_instance = mock_gitlab.Gitlab.return_value
    mock_instance.projects.get.return_value.commits.get.return_value.statuses.list.return_value = [
        {"status": "failed", "name": "job1", "allow_failure": True}
    ]

    result = Gitlab.check_build_status("owner", "repo", "ref")
    assert result is True
