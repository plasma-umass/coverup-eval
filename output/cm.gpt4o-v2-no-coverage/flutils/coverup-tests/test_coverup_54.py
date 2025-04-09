# file: flutils/codecs/raw_utf8_escape.py:158-162
# asked: {"lines": [159, 160, 161, 162], "branches": []}
# gained: {"lines": [159, 160, 161, 162], "branches": []}

import pytest
import codecs
from flutils.codecs.raw_utf8_escape import register, _get_codec_info

NAME = "raw_utf8_escape"

def test_register(monkeypatch):
    # Ensure the codec is not already registered
    def mock_getdecoder(name):
        raise LookupError

    monkeypatch.setattr(codecs, "getdecoder", mock_getdecoder)
    
    # Mock the codecs.register function
    def mock_register(func):
        assert func == _get_codec_info

    monkeypatch.setattr(codecs, "register", mock_register)
    
    # Call the register function
    register()

def test_register_already_registered(monkeypatch):
    # Mock the codecs.getdecoder to simulate the codec already being registered
    def mock_getdecoder(name):
        return lambda x: x

    monkeypatch.setattr(codecs, "getdecoder", mock_getdecoder)
    
    # Mock the codecs.register function to ensure it is not called
    def mock_register(func):
        raise AssertionError("register should not be called")

    monkeypatch.setattr(codecs, "register", mock_register)
    
    # Call the register function
    register()

def test_get_codec_info():
    # Test when the name matches
    codec_info = _get_codec_info(NAME)
    assert codec_info is not None
    assert codec_info.name == NAME

    # Test when the name does not match
    codec_info = _get_codec_info("other_name")
    assert codec_info is None
