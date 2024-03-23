# file youtube_dl/extractor/tudou.py:8-27
# lines [8, 9, 10, 11, 12, 13, 14, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27]
# branches []

import pytest
from youtube_dl.extractor.tudou import TudouPlaylistIE
from youtube_dl.utils import ExtractorError

def test_tudou_playlist_extraction(mocker):
    # Mock the _download_json method to return a fake playlist data
    fake_playlist_data = {
        'items': [
            {'icode': 'fake_icode1', 'kw': 'fake_title1'},
            {'icode': 'fake_icode2', 'kw': 'fake_title2'},
        ]
    }
    TudouPlaylistIE._download_json = mocker.Mock(return_value=fake_playlist_data)

    # Create an instance of the extractor
    ie = TudouPlaylistIE()

    # Mock TudouPlaylistIE._match_id to return a fake playlist ID
    mocker.patch.object(TudouPlaylistIE, '_match_id', return_value='fake_playlist_id')

    # Extract the playlist
    result = ie._real_extract('http://www.tudou.com/listplay/fake_playlist_id.html')

    # Assertions to check if the extraction is correct
    assert result['id'] == 'fake_playlist_id'
    assert len(result['entries']) == 2
    assert result['entries'][0]['url'] == 'http://www.tudou.com/programs/view/fake_icode1'
    assert result['entries'][0]['ie_key'] == 'Tudou'
    assert result['entries'][0]['id'] == 'fake_icode1'
    assert result['entries'][0]['title'] == 'fake_title1'
    assert result['entries'][1]['url'] == 'http://www.tudou.com/programs/view/fake_icode2'
    assert result['entries'][1]['ie_key'] == 'Tudou'
    assert result['entries'][1]['id'] == 'fake_icode2'
    assert result['entries'][1]['title'] == 'fake_title2'

    # Clean up by removing the mock
    mocker.stopall()
