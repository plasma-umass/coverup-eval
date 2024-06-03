# file youtube_dl/extractor/nrk.py:478-488
# lines [478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488]
# branches ['479->480', '479->481', '482->483', '482->488', '484->485', '484->486']

import pytest
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE, NRKIE
from youtube_dl.compat import compat_str

class MockNRKTVSerieBaseIE(NRKTVSerieBaseIE):
    def url_result(self, url, ie=None, video_id=None):
        return {'url': url, 'ie': ie, 'video_id': video_id}

@pytest.fixture
def mock_nrk_tv_serie_base_ie():
    return MockNRKTVSerieBaseIE()

def test_extract_entries_with_non_list(mock_nrk_tv_serie_base_ie):
    result = mock_nrk_tv_serie_base_ie._extract_entries(None)
    assert result == []

def test_extract_entries_with_invalid_nrk_id(mock_nrk_tv_serie_base_ie):
    entry_list = [{'prfId': None, 'episodeId': None}]
    result = mock_nrk_tv_serie_base_ie._extract_entries(entry_list)
    assert result == []

def test_extract_entries_with_valid_nrk_id(mock_nrk_tv_serie_base_ie):
    entry_list = [{'prfId': '12345', 'episodeId': None}]
    result = mock_nrk_tv_serie_base_ie._extract_entries(entry_list)
    assert len(result) == 1
    assert result[0]['url'] == 'nrk:12345'
    assert result[0]['ie'] == NRKIE.ie_key()
    assert result[0]['video_id'] == '12345'

def test_extract_entries_with_non_string_nrk_id(mock_nrk_tv_serie_base_ie):
    entry_list = [{'prfId': 12345, 'episodeId': None}]
    result = mock_nrk_tv_serie_base_ie._extract_entries(entry_list)
    assert result == []
