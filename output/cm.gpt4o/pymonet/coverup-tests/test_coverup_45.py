# file pymonet/utils.py:81-96
# lines [81, 92, 93, 94, 95]
# branches []

import pytest
from pymonet.utils import compose

def test_compose(mocker):
    # Mock functions to be composed
    mock_func1 = mocker.Mock(return_value=4)
    mock_func2 = mocker.Mock(return_value=3)
    mock_func3 = mocker.Mock(return_value=2)

    # Compose the functions
    result = compose(1, mock_func1, mock_func2, mock_func3)

    # Verify the result
    assert result == 4

    # Verify the order of function calls
    mock_func3.assert_called_once_with(1)
    mock_func2.assert_called_once_with(2)
    mock_func1.assert_called_once_with(3)
