# file flutils/codecs/raw_utf8_escape.py:158-162
# lines [158, 159, 160, 161, 162]
# branches []

import pytest
import codecs
from flutils.codecs.raw_utf8_escape import register, NAME

def test_register_codec():
    # Unregister the codec if it's already registered
    # This is necessary to ensure the test can be run multiple times
    # and is especially important in a test suite environment.
    try:
        codecs.lookup(NAME)
        codecs.unregister(codecs.lookup(NAME))
    except LookupError:
        pass  # Codec was not registered, nothing to unregister

    # Ensure the codec is not registered before calling register
    with pytest.raises(LookupError):
        codecs.getdecoder(NAME)

    # Call the register function
    register()

    # Now the codec should be registered, so this should not raise an error
    decoder = codecs.getdecoder(NAME)
    assert decoder is not None

    # Clean up: unregister the codec after the test
    codecs.unregister(codecs.lookup(NAME))
