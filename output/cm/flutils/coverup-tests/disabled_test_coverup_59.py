# file flutils/codecs/b64.py:110-115
# lines [112, 113, 114, 115]
# branches []

import pytest
from flutils.codecs.b64 import register
import codecs

# Assuming _get_codec_info is a private function in the flutils.codecs.b64 module
# We need to import it for the test
from flutils.codecs.b64 import _get_codec_info

def test_register_codec(mocker):
    # Mock the unregister method to prevent affecting the global state
    mocker.patch('codecs.unregister')

    # Ensure the codec is not registered
    with pytest.raises(LookupError):
        codecs.getdecoder('b64')

    # Register the codec
    register()

    # Ensure the codec is now registered
    decoder = codecs.getdecoder('b64')
    assert decoder is not None

    # Cleanup is not needed since we mocked the unregister method
