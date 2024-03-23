# file youtube_dl/extractor/nrk.py:454-474
# lines [454, 455, 457, 459, 460, 461, 462, 463, 464, 466, 467, 468, 469, 470, 471, 472, 474]
# branches []

import re
from unittest.mock import MagicMock

import pytest

from youtube_dl.extractor.nrk import NRKTVEpisodeIE
from youtube_dl.extractor.common import InfoExtractor


class MockNRKTVIE(InfoExtractor):
    _EPISODE_RE = r'(?P<id>[a-zA-Z0-9]{4,})'


@pytest.fixture
def mock_extractor(mocker):
    extractor = NRKTVEpisodeIE()
    mocker.patch.object(extractor, '_download_webpage', return_value='<html></html>')
    mocker.patch.object(extractor, '_search_json_ld', return_value={'@id': 'test_id'})
    mocker.patch.object(extractor, '_html_search_meta', return_value=None)
    mocker.patch.object(extractor, '_search_regex', return_value='test_id')
    mocker.patch('re.match', return_value=MagicMock(groups=lambda: ('display_id', '1', '2')))
    mocker.patch('youtube_dl.extractor.nrk.NRKTVIE._EPISODE_RE', MockNRKTVIE._EPISODE_RE)
    mocker.patch('youtube_dl.extractor.nrk.NRKIE.ie_key', return_value='NRK')
    return extractor


def test_nrk_tv_episode_extraction(mock_extractor):
    url = 'http://example.com/video'
    info = mock_extractor._real_extract(url)
    assert info['_type'] == 'url'
    assert info['id'] == 'test_id'
    assert info['url'] == 'nrk:test_id'
    assert info['ie_key'] == 'NRK'
    assert info['season_number'] == 1
    assert info['episode_number'] == 2
