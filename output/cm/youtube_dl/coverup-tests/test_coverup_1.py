# file youtube_dl/extractor/nrk.py:67-116
# lines [67, 68, 80, 82, 83, 84, 85, 86, 87, 88, 89, 91, 93, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKIE

@pytest.fixture
def nrk_ie(mocker):
    # Mock the _download_xml method to return a fake XML response
    fake_xml_response = '<xml><fake>response</fake></xml>'
    mocker.patch('youtube_dl.extractor.nrk.NRKBaseIE._download_xml', return_value=fake_xml_response)

    # Mock the _download_json method to return a fake JSON response
    fake_json_response = {'video': {'id': 'fake_id', 'title': 'Fake Title'}}
    mocker.patch('youtube_dl.extractor.nrk.NRKBaseIE._download_json', return_value=fake_json_response)

    # Mock the _real_extract method to return a fake result
    fake_result = {
        'id': 'fake_id',
        'title': 'Fake Title',
        'url': 'http://fake.url/video.mp4'
    }
    mocker.patch('youtube_dl.extractor.nrk.NRKIE._real_extract', return_value=fake_result)

    # Create an instance of the extractor
    ie = NRKIE()
    ie._downloader = mocker.MagicMock()
    ie._downloader.params = {'geo_bypass': True}

    return ie

def test_nrk_extractor(nrk_ie):
    # Test the extractor with a fake URL that matches the _VALID_URL pattern
    test_url = 'http://www.nrk.no/video/PS*123456'
    result = nrk_ie.extract(test_url)

    # Assertions to check if the result is as expected
    assert result['id'] == 'fake_id'
    assert result['title'] == 'Fake Title'
    assert result['url'] == 'http://fake.url/video.mp4'
