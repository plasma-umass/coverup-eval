# file thefuck/entrypoints/not_configured.py:29-33
# lines [29, 31, 32]
# branches []

import pytest
from unittest.mock import patch
from pathlib import Path
from tempfile import gettempdir
import getpass

# Import the function to be tested
from thefuck.entrypoints.not_configured import _get_not_configured_usage_tracker_path

def test_get_not_configured_usage_tracker_path(mocker):
    # Mock gettempdir and getpass.getuser to control their outputs
    mock_gettempdir = mocker.patch('thefuck.entrypoints.not_configured.gettempdir', return_value='/mocked/tempdir')
    mock_getuser = mocker.patch('thefuck.entrypoints.not_configured.getpass.getuser', return_value='mockeduser')

    # Call the function
    result = _get_not_configured_usage_tracker_path()

    # Verify the result
    expected_path = Path('/mocked/tempdir').joinpath('thefuck.last_not_configured_run_mockeduser')
    assert result == expected_path

    # Verify that the mocks were called
    mock_gettempdir.assert_called_once()
    mock_getuser.assert_called_once()
