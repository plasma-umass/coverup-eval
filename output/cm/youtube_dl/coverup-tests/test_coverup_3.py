# file youtube_dl/extractor/nrk.py:615-664
# lines [615, 616, 617, 619, 620, 621, 622, 623, 625, 626, 628, 629, 630, 631, 632, 633, 634, 635, 637, 638, 640, 641, 642, 643, 644, 646, 647, 649, 650, 651, 652, 653, 655, 656, 657, 658, 659, 660, 661, 662, 663, 664]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKTVSeriesIE

@pytest.fixture
def mock_extractor(mocker):
    extractor = NRKTVSeriesIE()
    mocker.patch.object(extractor, '_real_extract', return_value={'entries': []})
    extractor._downloader = mocker.MagicMock()
    extractor._downloader.params = {'geo_bypass': True}
    return extractor

def test_nrk_tv_series_ie(mock_extractor):
    test_urls = [
        'https://tv.nrk.no/serie/groenn-glede',
        'https://tv.nrk.no/serie/lindmo',
        'https://tv.nrk.no/serie/blank',
        'https://tv.nrk.no/serie/backstage',
        'https://tv.nrksuper.no/serie/labyrint',
        'https://tv.nrk.no/serie/broedrene-dal-og-spektralsteinene',
        'https://tv.nrk.no/serie/saving-the-human-race',
        'https://tv.nrk.no/serie/postmann-pat',
    ]

    for url in test_urls:
        info_dict = mock_extractor.extract(url)
        assert isinstance(info_dict, dict)
        assert 'entries' in info_dict
        assert isinstance(info_dict['entries'], list)
