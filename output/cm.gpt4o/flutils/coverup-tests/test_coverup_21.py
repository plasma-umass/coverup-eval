# file flutils/codecs/b64.py:110-115
# lines [110, 112, 113, 114, 115]
# branches []

import pytest
import codecs
from flutils.codecs.b64 import register

def test_register_codec(mocker):
    # Mock codecs.getdecoder to raise LookupError
    mock_getdecoder = mocker.patch('codecs.getdecoder', side_effect=LookupError)
    mock_register = mocker.patch('codecs.register')

    # Call the register function
    register()

    # Assert that codecs.getdecoder was called with the correct NAME
    mock_getdecoder.assert_called_once_with('b64')

    # Assert that codecs.register was called once
    mock_register.assert_called_once()

    # Clean up by resetting the mocks
    mock_getdecoder.reset_mock()
    mock_register.reset_mock()
