# file pymonet/utils.py:99-114
# lines [99, 110, 111, 112, 113]
# branches []

import pytest
from pymonet.utils import pipe

def test_pipe(mocker):
    # Mock functions to be used in the pipe
    mock_func1 = mocker.Mock(return_value=2)
    mock_func2 = mocker.Mock(return_value=3)
    mock_func3 = mocker.Mock(return_value=4)

    # Initial value
    initial_value = 1

    # Execute the pipe function
    result = pipe(initial_value, mock_func1, mock_func2, mock_func3)

    # Assertions to verify the correct execution and result
    assert result == 4
    mock_func1.assert_called_once_with(initial_value)
    mock_func2.assert_called_once_with(2)
    mock_func3.assert_called_once_with(3)
