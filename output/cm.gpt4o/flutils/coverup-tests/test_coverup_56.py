# file flutils/codecs/b64.py:99-107
# lines [100, 101, 102, 103, 104, 106, 107]
# branches ['100->101', '100->107']

import pytest
from flutils.codecs.b64 import _get_codec_info, NAME, decode, encode
import codecs

def test_get_codec_info():
    # Test when name matches NAME
    codec_info = _get_codec_info(NAME)
    assert codec_info is not None
    assert isinstance(codec_info, codecs.CodecInfo)
    assert codec_info.name == NAME
    assert codec_info.decode == decode
    assert codec_info.encode == encode

    # Test when name does not match NAME
    codec_info = _get_codec_info("invalid_name")
    assert codec_info is None
