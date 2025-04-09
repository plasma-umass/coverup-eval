# file: flutils/codecs/b64.py:99-107
# asked: {"lines": [99, 100, 101, 102, 103, 104, 106, 107], "branches": [[100, 101], [100, 107]]}
# gained: {"lines": [99, 100, 101, 102, 103, 104, 106, 107], "branches": [[100, 101], [100, 107]]}

import pytest
import codecs
from flutils.codecs.b64 import _get_codec_info, decode, encode, NAME

def test_get_codec_info_valid_name():
    codec_info = _get_codec_info(NAME)
    assert codec_info is not None
    assert codec_info.name == NAME
    assert codec_info.decode == decode
    assert codec_info.encode == encode

def test_get_codec_info_invalid_name():
    codec_info = _get_codec_info("invalid_name")
    assert codec_info is None
