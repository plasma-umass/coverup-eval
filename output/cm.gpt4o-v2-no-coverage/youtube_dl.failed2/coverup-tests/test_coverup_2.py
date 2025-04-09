# file: youtube_dl/extractor/itv.py:153-185
# asked: {"lines": [153, 154, 155, 156, 157, 158, 159, 161, 163, 165, 166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}
# gained: {"lines": [153, 154, 155, 156, 157, 158, 159, 161, 163, 165, 166, 168, 170, 171, 172, 175, 178, 180, 181, 183, 185], "branches": []}

import pytest
from youtube_dl.extractor.itv import ITVBTCCIE
from youtube_dl.extractor.brightcove import BrightcoveNewIE
from youtube_dl.utils import smuggle_url
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_dependencies(monkeypatch):
    mock_info_extractor = MagicMock()
    monkeypatch.setattr(ITVBTCCIE, '_download_webpage', mock_info_extractor._download_webpage)
    monkeypatch.setattr(ITVBTCCIE, '_og_search_title', mock_info_extractor._og_search_title)
    monkeypatch.setattr(ITVBTCCIE, 'url_result', mock_info_extractor.url_result)
    monkeypatch.setattr(ITVBTCCIE, 'playlist_result', mock_info_extractor.playlist_result)
    return mock_info_extractor

def test_real_extract(mock_dependencies):
    ie = ITVBTCCIE()
    url = 'http://www.itv.com/btcc/races/btcc-2018-all-the-action-from-brands-hatch'
    playlist_id = 'btcc-2018-all-the-action-from-brands-hatch'
    webpage = '<html>data-video-id="12345"</html>'
    title = 'BTCC 2018: All the action from Brands Hatch'
    
    mock_dependencies._download_webpage.return_value = webpage
    mock_dependencies._og_search_title.return_value = title
    
    result = ie._real_extract(url)
    
    mock_dependencies._download_webpage.assert_called_once_with(url, playlist_id)
    mock_dependencies._og_search_title.assert_called_once_with(webpage, fatal=False)
    mock_dependencies.url_result.assert_called_once_with(
        smuggle_url(ie.BRIGHTCOVE_URL_TEMPLATE % '12345', {
            'geo_ip_blocks': ['193.113.0.0/16', '54.36.162.0/23', '159.65.16.0/21'],
            'referrer': url,
        }),
        ie=BrightcoveNewIE.ie_key(), video_id='12345'
    )
    mock_dependencies.playlist_result.assert_called_once_with(
        [mock_dependencies.url_result.return_value], playlist_id, title
    )
    assert result == mock_dependencies.playlist_result.return_value
