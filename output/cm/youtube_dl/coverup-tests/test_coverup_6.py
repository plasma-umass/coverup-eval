# file youtube_dl/extractor/tvplay.py:25-74
# lines [25, 26, 27, 28, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74]
# branches []

import pytest
from youtube_dl.extractor.tvplay import TVPlayIE

@pytest.fixture
def mock_extractor(mocker):
    extractor = TVPlayIE()
    mocker.patch.object(extractor, '_real_extract', return_value={'id': '418113'})
    extractor._downloader = mocker.MagicMock()
    extractor._downloader.params = {'geo_bypass': True}
    return extractor

def test_tvplay_extractor(mock_extractor):
    test_url = 'http://www.tvplay.lv/parraides/vinas-melo-labak/418113?autostart=true'
    info_dict = mock_extractor.extract(test_url)
    assert info_dict['id'] == '418113'
    mock_extractor._real_extract.assert_called_once_with(test_url)
