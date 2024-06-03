# file youtube_dl/extractor/fourtube.py:24-24
# lines [24]
# branches []

import pytest
from youtube_dl.extractor.fourtube import FourTubeBaseIE
from youtube_dl.extractor.common import InfoExtractor

def test_fourtube_base_ie():
    class TestFourTubeBaseIE(FourTubeBaseIE):
        def _real_extract(self, url):
            return {
                'id': '1234',
                'title': 'Test Video',
                'url': 'http://example.com/video.mp4'
            }

    ie = TestFourTubeBaseIE()
    result = ie._real_extract('http://example.com/video/1234')

    assert result['id'] == '1234'
    assert result['title'] == 'Test Video'
    assert result['url'] == 'http://example.com/video.mp4'
