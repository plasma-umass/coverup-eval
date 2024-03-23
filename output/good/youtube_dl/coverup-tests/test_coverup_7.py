# file youtube_dl/extractor/zdf.py:195-236
# lines [195, 196, 198, 200, 202, 203, 204, 205, 207, 208, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 222, 223, 224, 225, 226, 228, 230, 231, 232, 233, 234, 235]
# branches ['202->203', '202->207', '213->214', '213->230', '214->215', '214->230', '216->217', '216->218', '223->224', '223->228']

import pytest
from youtube_dl.extractor.zdf import ZDFIE
from youtube_dl.utils import urljoin, try_get, int_or_none, unified_timestamp, url_or_none, merge_dicts
import re

@pytest.fixture
def mock_extractor(mocker):
    extractor = ZDFIE()
    mocker.patch.object(extractor, '_extract_ptmd', return_value={'info': 'mocked'})
    return extractor

def test_extract_entry_with_ptmd_template(mock_extractor, mocker):
    url = 'http://example.com/video'
    player = {'apiToken': 'mocked_token'}
    content = {
        'title': 'Test Title',
        'teaserHeadline': 'Test Headline',
        'mainVideoContent': {
            'http://zdf.de/rels/target': {
                'http://zdf.de/rels/streams/ptmd-template': 'http://example.com/template/{playerId}'
            }
        },
        'teaserImageRef': {
            'layouts': {
                '100x100': 'http://example.com/thumbnail_100x100',
                'invalid_layout': 'not_a_url'
            }
        },
        'editorialDate': '20210101 00:00:00'
    }
    video_id = '1234'

    mocker.patch('youtube_dl.extractor.zdf.urljoin', side_effect=urljoin)
    mocker.patch('youtube_dl.extractor.zdf.try_get', side_effect=try_get)
    mocker.patch('youtube_dl.extractor.zdf.int_or_none', side_effect=int_or_none)
    mocker.patch('youtube_dl.extractor.zdf.unified_timestamp', side_effect=unified_timestamp)
    mocker.patch('youtube_dl.extractor.zdf.url_or_none', side_effect=url_or_none)
    mocker.patch('youtube_dl.extractor.zdf.merge_dicts', side_effect=merge_dicts)

    result = mock_extractor._extract_entry(url, player, content, video_id)

    assert result['title'] == 'Test Title'
    assert result['thumbnails'] == [
        {
            'url': 'http://example.com/thumbnail_100x100',
            'format_id': '100x100',
            'width': 100,
            'height': 100
        }
    ]
    assert 'timestamp' not in result or result['timestamp'] == unified_timestamp('20210101 00:00:00')
    assert 'info' in result
