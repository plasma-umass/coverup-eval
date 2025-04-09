# file: flutils/codecs/raw_utf8_escape.py:158-162
# asked: {"lines": [158, 159, 160, 161, 162], "branches": []}
# gained: {"lines": [158, 159, 160, 161, 162], "branches": []}

import pytest
import codecs
from flutils.codecs.raw_utf8_escape import register, _get_codec_info, NAME

def test_register(monkeypatch):
    # Ensure the codec is not already registered
    def mock_getdecoder(name):
        if name == NAME:
            raise LookupError
        return None

    monkeypatch.setattr(codecs, 'getdecoder', mock_getdecoder)
    monkeypatch.setattr(codecs, 'register', lambda x: None)

    register()

    # Verify that the register function was called with _get_codec_info
    def mock_register(func):
        assert func == _get_codec_info

    monkeypatch.setattr(codecs, 'register', mock_register)
    register()
