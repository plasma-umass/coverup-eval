# file youtube_dl/extractor/hitrecord.py:35-68
# lines [36, 38, 39, 41, 42, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
# branches ['46->47', '46->53']

import pytest
from youtube_dl.extractor.hitrecord import HitRecordIE
from youtube_dl.utils import ExtractorError

@pytest.fixture
def mock_video_data():
    return {
        'title': 'Test Video',
        'source_url': {'mp4_url': 'http://test.mp4'},
        'tags': [{'text': 'tag1'}, {'text': 'tag2'}, {'not_text': 'tag3'}, 'tag4'],
        'body': '<p>Description</p>',
        'duration': '60000',
        'created_at_i': '1609459200',
        'user': {'username': 'testuser', 'id': '12345'},
        'total_views_count': '1000',
        'hearts_count': '100',
        'comments_count': '10'
    }

@pytest.fixture
def mock_extractor(mocker, mock_video_data):
    extractor = HitRecordIE()
    mocker.patch.object(extractor, '_download_json', return_value=mock_video_data)
    mocker.patch.object(extractor, '_match_id', return_value='123')
    return extractor

def test_hitrecord_extractor(mock_extractor):
    result = mock_extractor._real_extract('http://hitrecord.org/records/123')
    assert result['id'] == '123'
    assert result['url'] == 'http://test.mp4'
    assert result['title'] == 'Test Video'
    assert result['description'] == 'Description'
    assert result['duration'] == 60.0
    assert result['timestamp'] == 1609459200
    assert result['uploader'] == 'testuser'
    assert result['uploader_id'] == '12345'
    assert result['view_count'] == 1000
    assert result['like_count'] == 100
    assert result['comment_count'] == 10
    assert result['tags'] == ['tag1', 'tag2']
