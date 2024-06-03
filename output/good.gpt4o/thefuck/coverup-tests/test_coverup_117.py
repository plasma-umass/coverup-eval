# file thefuck/entrypoints/not_configured.py:36-43
# lines [38, 39, 41, 42, 43]
# branches []

import pytest
import six
import json
import time
from unittest import mock
from pathlib import Path
from thefuck.entrypoints.not_configured import _record_first_run, _get_shell_pid, _get_not_configured_usage_tracker_path

@pytest.fixture
def mock_get_shell_pid(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._get_shell_pid', return_value=12345)

@pytest.fixture
def mock_get_not_configured_usage_tracker_path(mocker, tmp_path):
    mock_path = tmp_path / "tracker.json"
    mocker.patch('thefuck.entrypoints.not_configured._get_not_configured_usage_tracker_path', return_value=mock_path)
    return mock_path

def test_record_first_run(mock_get_shell_pid, mock_get_not_configured_usage_tracker_path):
    _record_first_run()
    
    with mock_get_not_configured_usage_tracker_path.open('r') as tracker:
        info = json.load(tracker)
    
    assert info['pid'] == 12345
    assert 'time' in info
    assert isinstance(info['time'], float)
