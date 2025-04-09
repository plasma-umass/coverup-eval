# file: flutils/codecs/raw_utf8_escape.py:158-162
# asked: {"lines": [158, 159, 160, 161, 162], "branches": []}
# gained: {"lines": [158, 159, 160, 161, 162], "branches": []}

import pytest
import codecs
from flutils.codecs import raw_utf8_escape

def test_register(monkeypatch):
    # Ensure NAME is not registered
    NAME = "raw_utf8_escape"
    
    def mock_getdecoder(name):
        if name == NAME:
            raise LookupError
        return codecs.getdecoder(name)
    
    def mock_register(func):
        assert func == raw_utf8_escape._get_codec_info
    
    monkeypatch.setattr(codecs, "getdecoder", mock_getdecoder)
    monkeypatch.setattr(codecs, "register", mock_register)
    
    raw_utf8_escape.register()
