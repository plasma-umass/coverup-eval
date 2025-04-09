# file youtube_dl/extractor/tudou.py:30-49
# lines [30, 31, 32, 33, 34, 35, 36, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49]
# branches []

import pytest
from youtube_dl.extractor.tudou import TudouAlbumIE

def test_tudou_album(mocker):
    # Mock the _download_json method to return a fake album data
    fake_album_data = {
        'items': [
            {'icode': 'fake_icode1', 'kw': 'fake_kw1'},
            {'icode': 'fake_icode2', 'kw': 'fake_kw2'},
        ]
    }
    TudouAlbumIE._download_json = mocker.Mock(return_value=fake_album_data)

    # Create an instance of the extractor
    extractor = TudouAlbumIE()

    # Test the _real_extract method with a fake URL
    test_url = 'http://www.tudou.com/albumplay/fake_album_id.html'
    result = extractor._real_extract(test_url)

    # Assertions to check if the result is as expected
    assert isinstance(result, dict), "The result should be a dictionary"
    assert 'entries' in result, "The result should have an 'entries' key"
    assert len(result['entries']) == 2, "There should be two entries in the result"
    assert result['entries'][0]['_type'] == 'url', "The entry should be of type 'url'"
    assert result['entries'][0]['url'] == 'http://www.tudou.com/programs/view/fake_icode1', "The entry URL is incorrect"
    assert result['entries'][0]['ie_key'] == 'Tudou', "The entry ie_key is incorrect"
    assert result['entries'][0]['id'] == 'fake_icode1', "The entry id is incorrect"
    assert result['entries'][0]['title'] == 'fake_kw1', "The entry title is incorrect"

    # Clean up by resetting the mock
    mocker.resetall()
