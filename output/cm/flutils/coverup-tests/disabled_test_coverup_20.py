# file flutils/codecs/b64.py:110-115
# lines [110, 112, 113, 114, 115]
# branches []

import pytest
from flutils.codecs.b64 import register
import codecs

def test_register_codec():
    # Unregister the codec if it's already registered
    try:
        codecs.lookup('b64')
        codecs.unregister(codecs.lookup('b64'))
    except LookupError:
        pass

    # Ensure the codec is not registered before the test
    with pytest.raises(LookupError):
        codecs.getdecoder('b64')

    # Register the codec
    register()

    # Ensure the codec is now registered
    decoder = codecs.getdecoder('b64')
    assert decoder is not None

    # Clean up: unregister the codec after the test
    codecs.unregister(codecs.lookup('b64'))
