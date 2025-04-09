# file thefuck/entrypoints/not_configured.py:29-33
# lines [29, 31, 32]
# branches []

import os
import pytest
from pathlib import Path
from tempfile import gettempdir
from unittest.mock import patch
from thefuck.entrypoints.not_configured import _get_not_configured_usage_tracker_path

@pytest.fixture
def user_mock(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured.getpass.getuser', return_value='testuser')

@pytest.fixture
def cleanup_tracker_file():
    # Setup code before yield
    yield
    # Teardown code after yield
    tracker_file = Path(gettempdir()).joinpath('thefuck.last_not_configured_run_testuser')
    if tracker_file.exists():
        tracker_file.unlink()

def test_get_not_configured_usage_tracker_path(user_mock, cleanup_tracker_file):
    expected_path = Path(gettempdir()).joinpath('thefuck.last_not_configured_run_testuser')
    actual_path = _get_not_configured_usage_tracker_path()
    assert actual_path == expected_path
    assert actual_path.exists() == False
