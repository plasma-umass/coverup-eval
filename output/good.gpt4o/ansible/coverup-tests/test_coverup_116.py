# file lib/ansible/module_utils/api.py:69-93
# lines [69, 71, 72, 73, 75, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93]
# branches ['72->73', '72->75', '79->80', '79->82', '83->84', '83->89', '86->87', '86->88']

import pytest
import time
import sys
from unittest import mock

# Import the rate_limit function from the module
from ansible.module_utils.api import rate_limit

def test_rate_limit_decorator(mocker):
    # Mock time.sleep to avoid actual sleep during tests
    mock_sleep = mocker.patch('time.sleep', return_value=None)
    
    # Mock time.process_time or time.clock based on Python version
    if sys.version_info >= (3, 8):
        mock_time = mocker.patch('time.process_time', side_effect=[0.0, 0.5, 1.0, 1.5])
    else:
        mock_time = mocker.patch('time.clock', side_effect=[0.0, 0.5, 1.0, 1.5])
    
    @rate_limit(rate=1, rate_limit=2)
    def test_function():
        return "executed"
    
    # Call the decorated function and assert the return value
    assert test_function() == "executed"
    assert test_function() == "executed"
    
    # Check that time.sleep was called to enforce rate limiting
    assert mock_sleep.call_count == 2
    mock_sleep.assert_any_call(2.0)
    mock_sleep.assert_any_call(1.5)
    
    # Clean up by stopping the mocks
    mock_sleep.stop()
    mock_time.stop()
