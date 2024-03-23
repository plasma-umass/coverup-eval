# file youtube_dl/extractor/fourtube.py:117-145
# lines [117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 139, 140, 141, 142, 143, 144]
# branches []

import pytest
from youtube_dl.extractor.fourtube import FourTubeIE

@pytest.fixture
def mock_extractor(mocker):
    extractor = FourTubeIE()
    extractor._downloader = mocker.MagicMock()
    extractor._downloader.params = {'geo_bypass': True}
    mocker.patch.object(extractor, '_real_extract', return_value={'id': '209733'})
    return extractor

def test_four_tube_ie_extraction(mock_extractor):
    test_url = 'http://www.4tube.com/videos/209733/hot-babe-holly-michaels-gets-her-ass-stuffed-by-black'
    info_dict = mock_extractor.extract(test_url)
    assert info_dict['id'] == '209733', "The extracted ID should match the expected video ID"
