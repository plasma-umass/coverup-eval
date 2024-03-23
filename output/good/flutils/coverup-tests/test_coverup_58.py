# file flutils/codecs/raw_utf8_escape.py:158-162
# lines [159, 160, 161, 162]
# branches []

import codecs
import pytest

# Assuming the module flutils.codecs.raw_utf8_escape has a function named register
from flutils.codecs.raw_utf8_escape import register

# The name of the codec we are trying to register
NAME = "raw-utf8-escape"

def test_register_codec(mocker):
    # Mock the getdecoder to raise a LookupError
    mocker.patch.object(codecs, 'getdecoder', side_effect=LookupError)

    # Mock the register function to assert it's called
    mock_register = mocker.patch.object(codecs, 'register')

    # Call the register function which should now hit the except block
    register()

    # Assert that codecs.register was called with the correct codec info function
    mock_register.assert_called_once()

    # Cleanup: Unregister the codec if it was registered
    # This is just a placeholder for cleanup logic, as the actual cleanup would depend on
    # how the _get_codec_info function registers the codec and how to unregister it.
    # If the codec registration is global and affects subsequent tests, proper cleanup is required.
    # If the codec registration is local to a module or object, this may not be necessary.
    # For example, if there's a way to unregister, it might look like this:
    # codecs.unregister(_get_codec_info)
