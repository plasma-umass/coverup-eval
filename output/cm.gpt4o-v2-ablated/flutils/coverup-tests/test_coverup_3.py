# file: flutils/codecs/raw_utf8_escape.py:158-162
# asked: {"lines": [158, 159, 160, 161, 162], "branches": []}
# gained: {"lines": [158, 159, 160, 161, 162], "branches": []}

import codecs
import pytest
from flutils.codecs.raw_utf8_escape import register, _get_codec_info, NAME

def test_register(monkeypatch):
    # Ensure the codec is not already registered
    def mock_getdecoder(name):
        if name == NAME:
            raise LookupError
        return codecs.getdecoder(name)
    
    monkeypatch.setattr(codecs, 'getdecoder', mock_getdecoder)
    
    # Mock the register function to verify it gets called
    register_called = []

    def mock_register(func):
        register_called.append(func)
    
    monkeypatch.setattr(codecs, 'register', mock_register)
    
    # Call the function under test
    register()
    
    # Verify that the register function was called with _get_codec_info
    assert register_called == [_get_codec_info]

    # Clean up by ensuring the codec is not registered
    monkeypatch.undo()
