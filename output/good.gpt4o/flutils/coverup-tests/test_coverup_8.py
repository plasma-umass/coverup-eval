# file flutils/codecs/raw_utf8_escape.py:158-162
# lines [158, 159, 160, 161, 162]
# branches []

import pytest
import codecs
from flutils.codecs.raw_utf8_escape import register

def test_register_codec(mocker):
    # Mock codecs.getdecoder to raise LookupError
    mocker.patch('codecs.getdecoder', side_effect=LookupError)
    # Mock codecs.register to track if it gets called
    mock_register = mocker.patch('codecs.register')

    # Call the register function
    register()

    # Assert that codecs.register was called once
    mock_register.assert_called_once()

    # Clean up by resetting the mock
    mocker.stopall()
