# file: flutils/codecs/b64.py:110-115
# asked: {"lines": [110, 112, 113, 114, 115], "branches": []}
# gained: {"lines": [110, 112, 113, 114, 115], "branches": []}

import pytest
import codecs
from flutils.codecs import b64

def test_register(monkeypatch):
    # Ensure the codec is not already registered
    def mock_getdecoder(name):
        if name == b64.NAME:
            raise LookupError
        return None

    monkeypatch.setattr(codecs, 'getdecoder', mock_getdecoder)
    
    # Mock the codecs.register function
    def mock_register(func):
        assert func is b64._get_codec_info

    monkeypatch.setattr(codecs, 'register', mock_register)
    
    # Call the register function
    b64.register()
    
    # Ensure the codec is now registered
    def mock_getdecoder_success(name):
        if name == b64.NAME:
            return True
        raise LookupError

    monkeypatch.setattr(codecs, 'getdecoder', mock_getdecoder_success)
    
    # Call the register function again to hit the already registered branch
    b64.register()
