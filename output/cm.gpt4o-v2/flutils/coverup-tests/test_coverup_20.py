# file: flutils/codecs/raw_utf8_escape.py:147-155
# asked: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 155]]}
# gained: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 155]]}

import pytest
import codecs
from flutils.codecs.raw_utf8_escape import _get_codec_info, encode, decode

def test_get_codec_info_valid_name(monkeypatch):
    # Arrange
    name = "raw_utf8_escape"
    monkeypatch.setattr("flutils.codecs.raw_utf8_escape.NAME", name)
    
    # Act
    result = _get_codec_info(name)
    
    # Assert
    assert result is not None
    assert isinstance(result, codecs.CodecInfo)
    assert result.name == name
    assert result.encode == encode
    assert result.decode == decode

def test_get_codec_info_invalid_name():
    # Arrange
    name = "invalid_name"
    
    # Act
    result = _get_codec_info(name)
    
    # Assert
    assert result is None
