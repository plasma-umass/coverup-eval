# file pytutils/log.py:134-139
# lines [134, 135, 136, 138, 139]
# branches ['135->136', '135->138']

import pytest
from pytutils.log import _ensure_configured, configure

def test_ensure_configured_first_call(mocker):
    # Mock the configure function to ensure it is called
    mock_configure = mocker.patch('pytutils.log.configure')
    
    # Call the function to test the unconfigured branch
    _ensure_configured([])
    
    # Assert that configure was called
    mock_configure.assert_called_once()

def test_ensure_configured_subsequent_calls(mocker):
    # Mock the configure function to ensure it is not called
    mock_configure = mocker.patch('pytutils.log.configure')
    
    # Call the function with a non-empty list to simulate the configured state
    _ensure_configured([True])
    
    # Assert that configure was not called
    mock_configure.assert_not_called()
