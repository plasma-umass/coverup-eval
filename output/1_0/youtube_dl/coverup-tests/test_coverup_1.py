# file youtube_dl/extractor/dreisat.py:6-43
# lines [6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 33, 35, 37, 38, 39, 41, 42]
# branches []

import pytest
from youtube_dl.extractor.dreisat import DreiSatIE

@pytest.fixture
def mock_extractor(mocker):
    extractor_mock = mocker.patch('youtube_dl.extractor.dreisat.DreiSatIE._real_extract')
    extractor_mock.return_value = {
        'id': 'test',
        'title': 'Test Video',
        'url': 'http://test.url/video.mp4',
    }
    return extractor_mock

@pytest.fixture
def mock_downloader(mocker):
    downloader_mock = mocker.Mock()
    downloader_mock.params = {'geo_bypass': True}
    return downloader_mock

def test_dreisat_extractor(mock_extractor, mock_downloader):
    test_url = 'https://www.3sat.de/film/ab-18/10-wochen-sommer-108.html'
    extractor = DreiSatIE()
    extractor.set_downloader(mock_downloader)
    info = extractor.extract(test_url)
    assert mock_extractor.called
    assert info['id'] == 'test'
    assert info['title'] == 'Test Video'
    assert info['url'] == 'http://test.url/video.mp4'
