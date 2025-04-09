# file thefuck/entrypoints/not_configured.py:55-72
# lines [55, 57, 58, 59, 61, 62, 63, 64, 65, 66, 68, 69, 71, 72]
# branches ['58->59', '58->61', '68->69', '68->71']

import json
import os
import time
from pathlib import Path
from unittest.mock import patch

import pytest

from thefuck.entrypoints.not_configured import _is_second_run
from thefuck import const


@pytest.fixture
def tracker_path(tmp_path):
    tracker_file = tmp_path / 'the_fuck_usage_tracker.json'
    with patch('thefuck.entrypoints.not_configured._get_not_configured_usage_tracker_path') as mock_tracker_path:
        mock_tracker_path.return_value = tracker_file
        yield tracker_file


@pytest.fixture
def shell_pid():
    with patch('thefuck.entrypoints.not_configured._get_shell_pid') as mock_shell_pid:
        mock_shell_pid.return_value = 12345
        yield mock_shell_pid.return_value


@pytest.fixture
def previous_command():
    with patch('thefuck.entrypoints.not_configured._get_previous_command') as mock_previous_command:
        mock_previous_command.return_value = 'fuck'
        yield mock_previous_command.return_value


def test_is_second_run_false_when_tracker_does_not_exist(tracker_path, shell_pid):
    assert not _is_second_run()


def test_is_second_run_false_when_tracker_has_invalid_json(tracker_path, shell_pid):
    tracker_path.write_text('not a valid json')
    assert not _is_second_run()


def test_is_second_run_false_when_tracker_has_different_pid(tracker_path, shell_pid):
    tracker_path.write_text(json.dumps({'pid': shell_pid + 1, 'time': time.time()}))
    assert not _is_second_run()


def test_is_second_run_false_when_tracker_has_expired_time(tracker_path, shell_pid):
    tracker_path.write_text(json.dumps({'pid': shell_pid, 'time': time.time() - const.CONFIGURATION_TIMEOUT - 1}))
    assert not _is_second_run()


def test_is_second_run_true_when_previous_command_is_fuck(tracker_path, shell_pid, previous_command):
    tracker_path.write_text(json.dumps({'pid': shell_pid, 'time': time.time()}))
    assert _is_second_run()


def test_is_second_run_true_within_timeout(tracker_path, shell_pid):
    tracker_path.write_text(json.dumps({'pid': shell_pid, 'time': time.time()}))
    with patch('thefuck.entrypoints.not_configured._get_previous_command', return_value='not_fuck'):
        assert _is_second_run()
