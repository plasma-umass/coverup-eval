# file mimesis/random.py:48-54
# lines [48, 49, 54]
# branches []

import os
import pytest
from mimesis.random import Random

def test_urandom(mocker):
    # Mock os.urandom to ensure it is called with expected arguments and to control its output
    mock_urandom = mocker.patch('os.urandom', return_value=b'test_bytes')

    # Call the static method urandom of the Random class
    result = Random.urandom(10)

    # Assert that the mocked os.urandom was called with the correct arguments
    mock_urandom.assert_called_once_with(10)

    # Assert that the result is what we mocked os.urandom to return
    assert result == b'test_bytes'
