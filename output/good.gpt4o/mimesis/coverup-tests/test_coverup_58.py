# file mimesis/random.py:48-54
# lines [48, 49, 54]
# branches []

import os
import pytest
from unittest import mock
from mimesis.random import Random

def test_urandom(mocker):
    # Mock os.urandom to control its behavior
    mock_urandom = mocker.patch('os.urandom', return_value=b'\x00' * 16)
    
    # Call the static method urandom with a specific argument
    result = Random.urandom(16)
    
    # Assert that os.urandom was called with the correct argument
    mock_urandom.assert_called_once_with(16)
    
    # Assert that the result is as expected
    assert result == b'\x00' * 16
