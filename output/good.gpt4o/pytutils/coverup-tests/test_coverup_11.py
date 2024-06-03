# file pytutils/log.py:134-139
# lines [134, 135, 136, 138, 139]
# branches ['135->136', '135->138']

import pytest
from unittest.mock import patch
from pytutils.log import _ensure_configured, _CONFIGURED, configure

def test_ensure_configured_not_configured(mocker):
    # Mock the configure function
    mock_configure = mocker.patch('pytutils.log.configure')
    
    # Ensure _CONFIGURED is empty before the test
    _CONFIGURED.clear()
    
    # Call the function to test the branch where _has_configured is False
    _ensure_configured(_CONFIGURED)
    
    # Assert that configure was called
    mock_configure.assert_called_once()
    
    # Assert that _CONFIGURED now contains True
    assert _CONFIGURED == [True]
    
    # Clean up
    _CONFIGURED.clear()

def test_ensure_configured_already_configured(mocker):
    # Mock the configure function
    mock_configure = mocker.patch('pytutils.log.configure')
    
    # Ensure _CONFIGURED contains True before the test
    _CONFIGURED.append(True)
    
    # Call the function to test the branch where _has_configured is True
    _ensure_configured(_CONFIGURED)
    
    # Assert that configure was not called
    mock_configure.assert_not_called()
    
    # Assert that _CONFIGURED still contains True
    assert _CONFIGURED == [True]
    
    # Clean up
    _CONFIGURED.clear()
