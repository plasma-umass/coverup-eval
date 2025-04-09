# file: flutils/codecs/raw_utf8_escape.py:147-155
# asked: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 155]]}
# gained: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 155]]}

import pytest
import codecs
from flutils.codecs.raw_utf8_escape import _get_codec_info

NAME = "raw-utf-8-escape"
encode = lambda x: (x, len(x))
decode = lambda x: (x, len(x))

def test_get_codec_info_valid_name(monkeypatch):
    monkeypatch.setattr("flutils.codecs.raw_utf8_escape.NAME", NAME)
    monkeypatch.setattr("flutils.codecs.raw_utf8_escape.encode", encode)
    monkeypatch.setattr("flutils.codecs.raw_utf8_escape.decode", decode)
    
    result = _get_codec_info(NAME)
    assert result is not None
    assert result.name == NAME
    assert result.encode == encode
    assert result.decode == decode

def test_get_codec_info_invalid_name():
    result = _get_codec_info("invalid-name")
    assert result is None
