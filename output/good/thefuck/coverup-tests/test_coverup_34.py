# file thefuck/entrypoints/not_configured.py:36-43
# lines [36, 38, 39, 41, 42, 43]
# branches []

import json
import os
import pytest
from pathlib import Path
from unittest.mock import patch
from thefuck.entrypoints.not_configured import _record_first_run

@pytest.fixture
def mock_tracker_path(tmp_path):
    tracker_path = tmp_path / "not_configured_usage_tracker"
    with patch('thefuck.entrypoints.not_configured._get_not_configured_usage_tracker_path', return_value=tracker_path):
        yield tracker_path

@pytest.fixture
def mock_get_shell_pid():
    with patch('thefuck.entrypoints.not_configured._get_shell_pid', return_value=12345):
        yield

def test_record_first_run(mock_tracker_path, mock_get_shell_pid):
    _record_first_run()
    assert mock_tracker_path.exists()
    with mock_tracker_path.open() as tracker:
        info = json.load(tracker)
        assert info['pid'] == 12345
        assert 'time' in info
