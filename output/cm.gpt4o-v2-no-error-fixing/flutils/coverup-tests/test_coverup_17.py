# file: flutils/codecs/b64.py:99-107
# asked: {"lines": [99, 100, 101, 102, 103, 104, 106, 107], "branches": [[100, 101], [100, 107]]}
# gained: {"lines": [99, 100, 101, 102, 103, 104, 106, 107], "branches": [[100, 101], [100, 107]]}

import pytest
import codecs
from flutils.codecs import b64

def test_get_codec_info_valid_name(monkeypatch):
    def mock_name():
        return "b64"
    
    monkeypatch.setattr(b64, 'NAME', mock_name())
    
    codec_info = b64._get_codec_info("b64")
    assert codec_info is not None
    assert codec_info.name == "b64"
    assert codec_info.decode == b64.decode
    assert codec_info.encode == b64.encode

def test_get_codec_info_invalid_name():
    codec_info = b64._get_codec_info("invalid")
    assert codec_info is None
