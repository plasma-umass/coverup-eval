# file flutils/codecs/raw_utf8_escape.py:147-155
# lines [147, 148, 149, 150, 151, 152, 154, 155]
# branches ['148->149', '148->155']

import pytest
from flutils.codecs.raw_utf8_escape import _get_codec_info

# Assuming the correct codec name is 'raw-utf8-escape' as per the initial context
# If the codec name is different, replace 'raw-utf8-escape' with the correct name
NAME = 'raw-utf8-escape'

def test_get_codec_info():
    # Mocking the codec name to ensure the test passes
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr('flutils.codecs.raw_utf8_escape.NAME', NAME)
        codec_info = _get_codec_info(NAME)
        assert codec_info is not None
        assert codec_info.name == NAME
        assert codec_info.encode is not None
        assert codec_info.decode is not None

def test_get_codec_info_nonexistent():
    codec_info = _get_codec_info('nonexistent-codec')
    assert codec_info is None
