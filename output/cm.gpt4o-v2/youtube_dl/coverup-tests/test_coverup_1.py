# file: youtube_dl/extractor/glide.py:7-43
# asked: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42], "branches": []}
# gained: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 24, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 38, 39, 40, 41, 42], "branches": []}

import pytest
from youtube_dl.extractor.glide import GlideIE
from youtube_dl.extractor.common import InfoExtractor
from unittest.mock import patch, MagicMock

@pytest.fixture
def glide_ie():
    return GlideIE(downloader=MagicMock())

def test_glide_ie_real_extract(glide_ie, monkeypatch):
    url = 'http://share.glide.me/UZF8zlmuQbe4mr+7dCiQ0w=='
    video_id = 'UZF8zlmuQbe4mr+7dCiQ0w=='
    webpage = '''
    <html>
        <head><title>Damon's Glide message</title></head>
        <body>
            <source src="http://example.com/video.mp4" />
            <img id="video-thumbnail" src="http://example.com/thumbnail.jpg" />
        </body>
    </html>
    '''
    
    def mock_match_id(url):
        return video_id
    
    def mock_download_webpage(url, video_id):
        return webpage
    
    monkeypatch.setattr(glide_ie, '_match_id', mock_match_id)
    monkeypatch.setattr(glide_ie, '_download_webpage', mock_download_webpage)
    
    result = glide_ie._real_extract(url)
    
    assert result['id'] == video_id
    assert result['title'] == "Damon's Glide message"
    assert result['url'] == 'http://example.com/video.mp4'
    assert result['thumbnail'] == 'http://example.com/thumbnail.jpg'
