# file lib/ansible/module_utils/api.py:69-93
# lines [71, 72, 73, 75, 76, 78, 79, 80, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93]
# branches ['72->73', '72->75', '79->80', '79->82', '83->84', '83->89', '86->87', '86->88']

import pytest
import time
from unittest.mock import patch
from ansible.module_utils.api import rate_limit

@pytest.fixture
def mock_time_process_time(mocker):
    mock = mocker.patch('time.process_time', return_value=0)
    yield mock
    mock.stop()

@pytest.fixture
def mock_time_sleep(mocker):
    mock = mocker.patch('time.sleep')
    yield mock
    mock.stop()

def test_rate_limit_with_rate_and_rate_limit(mock_time_process_time, mock_time_sleep):
    @rate_limit(rate=1, rate_limit=2)
    def test_function():
        return "test"

    # Call the function twice to trigger the rate limiting
    assert test_function() == "test"
    assert test_function() == "test"

    # Assert that time.process_time was called and that time.sleep was called with the correct argument
    assert mock_time_process_time.call_count > 0
    sleep_time = 2.0 - (mock_time_process_time.return_value - mock_time_process_time.return_value)
    mock_time_sleep.assert_called_with(sleep_time)
