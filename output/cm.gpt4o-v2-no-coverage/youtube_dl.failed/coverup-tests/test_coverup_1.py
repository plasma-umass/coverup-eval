# file: youtube_dl/extractor/soundgasm.py:9-54
# asked: {"lines": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 28, 30, 31, 32, 34, 35, 36, 38, 39, 41, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53], "branches": []}
# gained: {"lines": [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 24, 25, 26, 28, 30, 31, 32, 34, 35, 36, 38, 39, 41, 43, 44, 46, 47, 48, 49, 50, 51, 52, 53], "branches": []}

import pytest
from youtube_dl.extractor.soundgasm import SoundgasmIE
from youtube_dl.extractor.common import InfoExtractor
import re

class TestSoundgasmIE:
    @pytest.fixture
    def soundgasm_ie(self):
        ie = SoundgasmIE()
        ie._downloader = type('MockDownloader', (object,), {'params': {'no_color': True}})()
        return ie

    @pytest.fixture
    def mock_webpage(self, monkeypatch):
        def mock_download_webpage(self, url, display_id):
            return '''
                <div class="jp-title">Piano sample</div>
                <div class="jp-description">Royalty Free Sample Music</div>
                m4a: 'http://example.com/audio/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a'
            '''
        monkeypatch.setattr(InfoExtractor, '_download_webpage', mock_download_webpage)

    def test_real_extract(self, soundgasm_ie, mock_webpage):
        url = 'http://soundgasm.net/u/ytdl/Piano-sample'
        result = soundgasm_ie._real_extract(url)
        
        assert result['id'] == '88abd86ea000cafe98f96321b23cc1206cbcbcc9'
        assert result['display_id'] == 'Piano-sample'
        assert result['url'] == 'http://example.com/audio/88abd86ea000cafe98f96321b23cc1206cbcbcc9.m4a'
        assert result['vcodec'] == 'none'
        assert result['title'] == 'Piano sample'
        assert result['description'] == 'Royalty Free Sample Music'
        assert result['uploader'] == 'ytdl'
