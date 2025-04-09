# file py_backwards/utils/helpers.py:39-40
# lines [39, 40]
# branches []

import pytest
import sys
from unittest import mock
from py_backwards.utils import helpers

def test_warn(mocker):
    mock_message = "This is a warning"
    mock_warn_message = "Warning: This is a warning"
    
    # Mock the messages.warn function to return a specific string
    mocker.patch('py_backwards.utils.helpers.messages.warn', return_value=mock_warn_message)
    
    # Mock sys.stderr to capture the output
    mock_stderr = mocker.patch('sys.stderr', new_callable=mock.Mock)
    
    # Call the warn function
    helpers.warn(mock_message)
    
    # Assert that the messages.warn function was called with the correct argument
    helpers.messages.warn.assert_called_once_with(mock_message)
    
    # Capture the actual calls to sys.stderr.write
    actual_calls = mock_stderr.write.call_args_list
    
    # Assert that the correct message was printed to stderr in two parts
    assert actual_calls[0] == mock.call(mock_warn_message)
    assert actual_calls[1] == mock.call('\n')
