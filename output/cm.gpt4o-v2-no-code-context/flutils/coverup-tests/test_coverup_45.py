# file: flutils/codecs/b64.py:110-115
# asked: {"lines": [110, 112, 113, 114, 115], "branches": []}
# gained: {"lines": [110, 112, 113, 114, 115], "branches": []}

import pytest
import codecs
from flutils.codecs.b64 import register
from unittest import mock

def test_register_codec_already_registered(monkeypatch):
    # Ensure the codec is already registered
    monkeypatch.setattr(codecs, 'getdecoder', lambda name: (lambda input: (b'', len(input))) if name == 'b64' else None)
    
    # Call the register function
    register()
    
    # Assert that the codec is still registered
    assert codecs.getdecoder('b64') is not None

def test_register_codec_not_registered(monkeypatch):
    # Ensure the codec is not registered initially
    original_getdecoder = codecs.getdecoder
    def mock_getdecoder(name):
        if name == 'b64':
            raise LookupError
        return original_getdecoder(name)
    
    monkeypatch.setattr(codecs, 'getdecoder', mock_getdecoder)
    mock_register = mock.Mock()
    monkeypatch.setattr(codecs, 'register', mock_register)
    
    # Call the register function
    register()
    
    # Assert that the codec registration was attempted
    mock_register.assert_called_once()
