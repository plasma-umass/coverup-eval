# file thefuck/entrypoints/not_configured.py:55-72
# lines [57, 58, 59, 61, 62, 63, 64, 65, 66, 68, 69, 71, 72]
# branches ['58->59', '58->61', '68->69', '68->71']

import pytest
import json
import time
from unittest import mock
from pathlib import Path
from thefuck.entrypoints.not_configured import _is_second_run, _get_not_configured_usage_tracker_path, _get_shell_pid, _get_previous_command
import thefuck.const as const

@pytest.fixture
def mock_tracker_path(tmp_path, mocker):
    tracker_path = tmp_path / "tracker.json"
    mocker.patch('thefuck.entrypoints.not_configured._get_not_configured_usage_tracker_path', return_value=tracker_path)
    return tracker_path

@pytest.fixture
def mock_shell_pid(mocker):
    mock_pid = 12345
    mocker.patch('thefuck.entrypoints.not_configured._get_shell_pid', return_value=mock_pid)
    return mock_pid

@pytest.fixture
def mock_previous_command(mocker):
    mocker.patch('thefuck.entrypoints.not_configured._get_previous_command', return_value='fuck')

def test_is_second_run_no_tracker(mock_tracker_path):
    assert not _is_second_run()

def test_is_second_run_invalid_json(mock_tracker_path):
    mock_tracker_path.write_text("invalid json")
    assert not _is_second_run()

def test_is_second_run_wrong_pid(mock_tracker_path, mock_shell_pid):
    info = {"pid": mock_shell_pid + 1, "time": time.time()}
    mock_tracker_path.write_text(json.dumps(info))
    assert not _is_second_run()

def test_is_second_run_correct_conditions(mock_tracker_path, mock_shell_pid, mock_previous_command):
    info = {"pid": mock_shell_pid, "time": time.time()}
    mock_tracker_path.write_text(json.dumps(info))
    assert _is_second_run()

def test_is_second_run_timeout(mock_tracker_path, mock_shell_pid, mocker):
    mocker.patch('thefuck.entrypoints.not_configured._get_previous_command', return_value='some_other_command')
    info = {"pid": mock_shell_pid, "time": time.time() - const.CONFIGURATION_TIMEOUT - 1}
    mock_tracker_path.write_text(json.dumps(info))
    assert not _is_second_run()
