# file youtube_dl/extractor/nrk.py:694-733
# lines [695, 696, 697, 699, 700, 701, 702, 703, 704, 705, 706, 707, 708, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 727, 728, 729, 730, 732, 733]
# branches ['715->716', '715->727', '716->717', '716->729', '718->719', '718->722', '720->721', '720->722', '722->716', '722->723', '727->728', '727->729']

import pytest
from youtube_dl.extractor.nrk import NRKTVSeriesIE, NRKTVSeasonIE
from youtube_dl.utils import try_get

@pytest.fixture
def mock_call_api(mocker):
    mocker.patch.object(NRKTVSeriesIE, '_call_api', side_effect=lambda *args, **kwargs: {
        'titles': {'title': 'Test Title', 'subtitle': 'Test Subtitle'},
        '_embedded': {
            'seasons': [
                {'_links': {'seasons': [{'href': '/test_season_1', 'title': 'Season 1'}]}},
                {'_links': {'seasons': [{'href': '/test_season_2', 'title': 'Season 2'}]}}
            ],
            'extraMaterial': {}
        },
        '_links': {
            'seasons': [
                {'href': '/test_season_1', 'title': 'Season 1'},
                {'href': '/test_season_2', 'title': 'Season 2'},
                {'href': '/test_season_3', 'title': 'Season 3'}
            ]
        },
        'type': 'series',
        'seriesType': 'series'
    })
    mocker.patch('youtube_dl.extractor.nrk.urljoin', side_effect=lambda base, url: f'https://tv.nrk.no{url}')
    mocker.patch('youtube_dl.extractor.nrk.compat_str', side_effect=lambda x: str(x))
    mocker.patch('youtube_dl.extractor.nrk.NRKTVSeasonIE.ie_key', return_value='NRKTVSeason')

def test_nrk_series_extraction(mock_call_api):
    url = 'https://tv.nrk.no/serie/test_series'
    ie = NRKTVSeriesIE()
    result = ie._real_extract(url)
    assert result['id'] == 'test_series'
    assert result['title'] == 'Test Title'
    assert result['description'] == 'Test Subtitle'
    assert len(result['entries']) == 3  # 3 from linked seasons
    assert result['entries'][0]['_type'] == 'url'
    assert result['entries'][0]['url'] == 'https://tv.nrk.no/test_season_1'
    assert result['entries'][0]['ie_key'] == 'NRKTVSeason'
    assert result['entries'][0]['title'] == 'Season 1'
    assert result['entries'][1]['url'] == 'https://tv.nrk.no/test_season_2'
    assert result['entries'][1]['title'] == 'Season 2'
    assert result['entries'][2]['url'] == 'https://tv.nrk.no/test_season_3'
    assert result['entries'][2]['title'] == 'Season 3'
