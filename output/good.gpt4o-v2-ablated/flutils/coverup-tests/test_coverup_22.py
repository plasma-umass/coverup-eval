# file: flutils/codecs/b64.py:110-115
# asked: {"lines": [110, 112, 113, 114, 115], "branches": []}
# gained: {"lines": [110, 112, 113, 114, 115], "branches": []}

import codecs
import pytest
from flutils.codecs.b64 import register

def test_register(monkeypatch):
    # Ensure the codec is not already registered
    def mock_getdecoder(name):
        if name == "b64":
            raise LookupError
        return None

    monkeypatch.setattr(codecs, "getdecoder", mock_getdecoder)
    
    # Mock the register function to verify it gets called
    register_called = []

    def mock_register(func):
        register_called.append(True)

    monkeypatch.setattr(codecs, "register", mock_register)

    # Call the function under test
    register()

    # Assert that the register function was called
    assert register_called == [True]

    # Clean up by removing the mock
    monkeypatch.undo()
