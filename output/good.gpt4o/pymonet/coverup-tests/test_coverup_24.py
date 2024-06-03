# file pymonet/utils.py:140-165
# lines [140, 154, 156, 157, 158, 159, 160, 161, 163, 165]
# branches ['158->159', '158->160']

import pytest
from unittest.mock import Mock
from pymonet.utils import memoize

def test_memoize(mocker):
    # Mock the function to be memoized
    mock_fn = Mock()
    mock_fn.side_effect = lambda x: x * 2

    # Create a key function for equality check
    def key_fn(a, b):
        return a == b

    # Memoize the mock function
    memoized_fn = memoize(mock_fn, key=key_fn)

    # Call the memoized function with an argument
    result1 = memoized_fn(2)
    assert result1 == 4
    mock_fn.assert_called_once_with(2)

    # Call the memoized function with the same argument to hit the cache
    result2 = memoized_fn(2)
    assert result2 == 4
    mock_fn.assert_called_once_with(2)  # Ensure the original function is not called again

    # Call the memoized function with a different argument
    result3 = memoized_fn(3)
    assert result3 == 6
    assert mock_fn.call_count == 2  # Ensure the original function is called again

    # Clean up by resetting the mock
    mock_fn.reset_mock()
