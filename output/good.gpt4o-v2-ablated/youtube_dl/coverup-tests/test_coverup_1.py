# file: youtube_dl/extractor/tf1.py:43-87
# asked: {"lines": [43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 55, 56, 57, 58, 59, 60, 62, 64, 65, 66, 67, 68, 69, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], "branches": [[56, 57], [56, 62], [58, 59], [58, 60], [65, 66], [65, 74], [67, 68], [67, 69]]}
# gained: {"lines": [43, 44, 45, 46, 47, 48, 49, 50, 52, 53, 55, 56, 57, 58, 59, 60, 62, 64, 65, 66, 67, 69, 70, 71, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86], "branches": [[56, 57], [56, 62], [58, 59], [58, 60], [65, 66], [65, 74], [67, 69]]}

import pytest
import json
import re
from youtube_dl.extractor.tf1 import TF1IE
from youtube_dl.utils import int_or_none, parse_iso8601, try_get

@pytest.fixture
def mock_download_json(mocker):
    return mocker.patch('youtube_dl.extractor.tf1.TF1IE._download_json')

@pytest.fixture
def mock_valid_url(mocker):
    return mocker.patch('youtube_dl.extractor.tf1.TF1IE._VALID_URL', re.compile(r'https?://www\.tf1\.fr/([^/]+)/([^/]+)'))

@pytest.fixture
def tf1ie_instance():
    return TF1IE()

def test_real_extract(mock_download_json, mock_valid_url, tf1ie_instance):
    url = 'https://www.tf1.fr/program_slug/slug'
    mock_download_json.return_value = {
        'data': {
            'videoBySlug': {
                'streamId': '12345',
                'tags': [{'label': 'tag1'}, {'label': 'tag2'}, {}],
                'decoration': {
                    'image': {
                        'sources': [{'url': 'http://example.com/thumb1.jpg', 'width': 640}, {'url': 'http://example.com/thumb2.jpg'}]
                    },
                    'description': 'A description',
                    'programLabel': 'A series'
                },
                'title': 'A title',
                'date': '2023-01-01T00:00:00Z',
                'publicPlayingInfos': {'duration': 3600},
                'season': '1',
                'episode': '2'
            }
        }
    }

    result = tf1ie_instance._real_extract(url)

    assert result['_type'] == 'url_transparent'
    assert result['id'] == '12345'
    assert result['url'] == 'wat:12345'
    assert result['title'] == 'A title'
    assert result['description'] == 'A description'
    assert result['timestamp'] == parse_iso8601('2023-01-01T00:00:00Z')
    assert result['duration'] == 3600
    assert result['tags'] == ['tag1', 'tag2']
    assert result['series'] == 'A series'
    assert result['season_number'] == 1
    assert result['episode_number'] == 2
    assert result['thumbnails'] == [
        {'url': 'http://example.com/thumb1.jpg', 'width': 640},
        {'url': 'http://example.com/thumb2.jpg', 'width': None}
    ]
