# file: youtube_dl/extractor/thestar.py:7-36
# asked: {"lines": [29, 30, 31, 32, 33, 34, 35, 36], "branches": []}
# gained: {"lines": [29, 30, 31, 32, 33, 34, 35, 36], "branches": []}

import pytest
from youtube_dl.extractor.thestar import TheStarIE
from youtube_dl.extractor.common import InfoExtractor
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_info_extractor(monkeypatch):
    mock_ie = MagicMock(spec=InfoExtractor)
    monkeypatch.setattr(TheStarIE, '_match_id', mock_ie._match_id)
    monkeypatch.setattr(TheStarIE, '_download_webpage', mock_ie._download_webpage)
    monkeypatch.setattr(TheStarIE, '_search_regex', mock_ie._search_regex)
    monkeypatch.setattr(TheStarIE, 'url_result', mock_ie.url_result)
    return mock_ie

def test_real_extract(mock_info_extractor):
    url = 'http://www.thestar.com/life/2016/02/01/mankind-why-this-woman-started-a-men-s-skincare-line.html'
    display_id = 'mankind-why-this-woman-started-a-men-s-skincare-line'
    webpage = '<html>mainartBrightcoveVideoId: "4732393888001"</html>'
    brightcove_id = '4732393888001'
    brightcove_url = TheStarIE.BRIGHTCOVE_URL_TEMPLATE % brightcove_id

    mock_info_extractor._match_id.return_value = display_id
    mock_info_extractor._download_webpage.return_value = webpage
    mock_info_extractor._search_regex.return_value = brightcove_id
    mock_info_extractor.url_result.return_value = {
        '_type': 'url',
        'url': brightcove_url,
        'ie_key': 'BrightcoveNew',
        'id': brightcove_id
    }

    ie = TheStarIE()
    result = ie._real_extract(url)

    mock_info_extractor._match_id.assert_called_once_with(url)
    mock_info_extractor._download_webpage.assert_called_once_with(url, display_id)
    mock_info_extractor._search_regex.assert_called_once_with(
        r'mainartBrightcoveVideoId["\']?\s*:\s*["\']?(\d+)',
        webpage, 'brightcove id'
    )
    mock_info_extractor.url_result.assert_called_once_with(
        brightcove_url, 'BrightcoveNew', brightcove_id
    )

    assert result == {
        '_type': 'url',
        'url': brightcove_url,
        'ie_key': 'BrightcoveNew',
        'id': brightcove_id
    }
