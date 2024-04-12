# file youtube_dl/extractor/archiveorg.py:49-95
# lines [50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 72, 73, 75, 76, 78, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 91, 92, 93, 95]
# branches ['58->59', '58->61', '61->63', '61->66', '67->68', '67->72', '86->87', '86->95']

import pytest
from youtube_dl.extractor.archiveorg import ArchiveOrgIE
from youtube_dl.utils import ExtractorError

@pytest.fixture
def mock_extractor(mocker):
    extractor = ArchiveOrgIE()
    mocker.patch.object(extractor, '_match_id', return_value='test_video')
    mocker.patch.object(extractor, '_download_webpage', return_value='<div class="js-play8-playlist" value="[{}]"></div>')
    mocker.patch.object(extractor, '_download_json', return_value={'metadata': {}})
    mocker.patch.object(extractor, '_parse_json', return_value=[{'id': 'test_video'}])
    mocker.patch.object(extractor, '_parse_html5_media_entries', return_value=[{'id': 'test_video'}])
    mocker.patch.object(extractor, '_parse_jwplayer_data', return_value={'id': 'test_video'})
    mocker.patch('youtube_dl.extractor.common.InfoExtractor._search_regex', return_value='<div class="js-play8-playlist" value="[{}]"></div>')
    mocker.patch('youtube_dl.extractor.common.InfoExtractor._downloader', return_value=mocker.Mock(params={}))
    return extractor

def test_archiveorg_extractor(mock_extractor):
    test_url = 'http://archive.org/details/test_video'
    info = mock_extractor._real_extract(test_url)
    assert info['id'] == 'test_video'
    assert mock_extractor._download_webpage.called
    assert mock_extractor._download_json.called
    assert mock_extractor._parse_json.called or mock_extractor._parse_html5_media_entries.called
    assert mock_extractor._parse_jwplayer_data.called or mock_extractor._parse_html5_media_entries.called
