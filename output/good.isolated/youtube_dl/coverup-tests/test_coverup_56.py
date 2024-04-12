# file youtube_dl/extractor/zdf.py:318-320
# lines [320]
# branches []

import pytest
from youtube_dl.extractor.zdf import ZDFChannelIE, ZDFIE

def test_zdf_channel_ie_suitable(mocker):
    # Mock ZDFIE.suitable to return True
    mocker.patch('youtube_dl.extractor.zdf.ZDFIE.suitable', return_value=True)
    assert not ZDFChannelIE.suitable('http://example.com/video')  # Should return False

    # Mock ZDFIE.suitable to return False
    mocker.patch('youtube_dl.extractor.zdf.ZDFIE.suitable', return_value=False)
    # We need to mock the super call to return a value, let's say True
    mocker.patch('youtube_dl.extractor.zdf.super', return_value=mocker.Mock(suitable=lambda x: True))
    assert ZDFChannelIE.suitable('http://example.com/video')  # Should return True
