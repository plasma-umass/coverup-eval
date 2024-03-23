# file flutils/codecs/b64.py:99-107
# lines [100, 101, 102, 103, 104, 106, 107]
# branches ['100->101', '100->107']

import pytest
from flutils.codecs.b64 import _get_codec_info, NAME

def test_get_codec_info():
    # Test the case where the name matches and the codec info is returned
    codec_info = _get_codec_info(NAME)
    assert codec_info is not None
    assert codec_info.name == NAME
    assert codec_info.encode is not None
    assert codec_info.decode is not None

    # Test the case where the name does not match and None is returned
    codec_info = _get_codec_info("nonexistent_codec_name")
    assert codec_info is None
