# file pymonet/monad_try.py:53-64
# lines [62, 63, 64]
# branches ['62->63', '62->64']

import pytest
from pymonet.monad_try import Try

def test_try_bind_success(mocker):
    # Mock a successful Try instance
    mock_try = mocker.Mock(spec=Try)
    mock_try.is_success = True
    mock_try.value = 42

    # Define a binder function
    def binder(x):
        return Try.of(lambda: x + 1)

    # Bind the function to the Try instance
    result = Try.bind(mock_try, binder)

    # Assertions to verify the postconditions
    assert result.is_success
    assert result.value == 43

def test_try_bind_failure(mocker):
    # Mock a failed Try instance
    mock_try = mocker.Mock(spec=Try)
    mock_try.is_success = False

    # Define a binder function
    def binder(x):
        return Try.of(lambda: x + 1)

    # Bind the function to the Try instance
    result = Try.bind(mock_try, binder)

    # Assertions to verify the postconditions
    assert result == mock_try
