# file: youtube_dl/extractor/usanetwork.py:7-24
# asked: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22], "branches": []}
# gained: {"lines": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 22], "branches": []}

import pytest
from youtube_dl.extractor.usanetwork import USANetworkIE
from youtube_dl.extractor.nbc import NBCIE
from youtube_dl import YoutubeDL

@pytest.fixture
def usa_network_ie():
    ydl = YoutubeDL({'geo_bypass': True})
    return USANetworkIE(downloader=ydl)

def test_usa_network_ie_valid_url(usa_network_ie):
    test_url = 'https://www.usanetwork.com/peacock-trailers/video/intelligence-trailer/4185302'
    assert usa_network_ie.suitable(test_url)
    assert usa_network_ie._match_id(test_url) == '4185302'

def test_usa_network_ie_test_cases(usa_network_ie, monkeypatch):
    test_case = USANetworkIE._TESTS[0]
    url = test_case['url']
    info_dict = test_case['info_dict']
    params = test_case['params']

    def mock_real_extract(self, url):
        return info_dict

    monkeypatch.setattr(NBCIE, '_real_extract', mock_real_extract)

    result = usa_network_ie.extract(url)
    assert result['id'] == info_dict['id']
    assert result['ext'] == info_dict['ext']
    assert result['title'] == info_dict['title']
    assert result['description'] == info_dict['description']
    assert result['upload_date'] == info_dict['upload_date']
    assert result['timestamp'] == info_dict['timestamp']
    assert result['uploader'] == info_dict['uploader']
