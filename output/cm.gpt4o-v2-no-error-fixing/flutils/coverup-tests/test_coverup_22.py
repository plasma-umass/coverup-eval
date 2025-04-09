# file: flutils/codecs/b64.py:110-115
# asked: {"lines": [110, 112, 113, 114, 115], "branches": []}
# gained: {"lines": [110, 112, 113, 114, 115], "branches": []}

import pytest
import codecs
from flutils.codecs import b64

def test_register(monkeypatch):
    # Ensure the codec is not already registered
    def mock_getdecoder(name):
        raise LookupError

    monkeypatch.setattr(codecs, 'getdecoder', mock_getdecoder)
    
    # Mock the register function to track if it gets called
    register_called = []

    def mock_register(func):
        register_called.append(True)

    monkeypatch.setattr(codecs, 'register', mock_register)
    
    # Call the register function
    b64.register()
    
    # Assert that the register function was called
    assert register_called == [True]

    # Clean up by removing the mock
    monkeypatch.undo()
