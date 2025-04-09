# file: flutils/codecs/raw_utf8_escape.py:147-155
# asked: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 155]]}
# gained: {"lines": [147, 148, 149, 150, 151, 152, 154, 155], "branches": [[148, 149], [148, 155]]}

import pytest
import codecs
from flutils.codecs.raw_utf8_escape import _get_codec_info, NAME, encode, decode

def test_get_codec_info_valid_name():
    codec_info = _get_codec_info(NAME)
    assert codec_info is not None
    assert codec_info.name == NAME
    assert codec_info.encode == encode
    assert codec_info.decode == decode

def test_get_codec_info_invalid_name():
    codec_info = _get_codec_info("invalid_name")
    assert codec_info is None
