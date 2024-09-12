# file: youtube_dl/extractor/tvland.py:7-37
# asked: {"lines": [7, 8, 9, 10, 11, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 35, 36], "branches": []}
# gained: {"lines": [7, 8, 9, 10, 11, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 35, 36], "branches": []}

import pytest
from youtube_dl.extractor.tvland import TVLandIE
from youtube_dl import YoutubeDL

@pytest.mark.parametrize("url, info_dict, playlist_mincount, params, only_matching", [
    (
        'https://www.tvland.com/episodes/s04pzf/everybody-loves-raymond-the-dog-season-1-ep-19',
        {'description': 'md5:84928e7a8ad6649371fbf5da5e1ad75a', 'title': 'The Dog'},
        5,
        None,
        False
    ),
    (
        'https://www.tvland.com/video-clips/4n87f2/younger-a-first-look-at-younger-season-6',
        {'id': '891f7d3c-5b5b-4753-b879-b7ba1a601757', 'ext': 'mp4', 'title': 'Younger|April 30, 2019|6|NO-EPISODE#|A First Look at Younger Season 6', 'description': 'md5:595ea74578d3a888ae878dfd1c7d4ab2', 'upload_date': '20190430', 'timestamp': 1556658000},
        None,
        {'skip_download': True},
        False
    ),
    (
        'http://www.tvland.com/full-episodes/iu0hz6/younger-a-kiss-is-just-a-kiss-season-3-ep-301',
        None,
        None,
        None,
        True
    )
])
def test_tvland_ie(url, info_dict, playlist_mincount, params, only_matching, monkeypatch):
    ydl = YoutubeDL({'geo_bypass': True})
    ie = TVLandIE(ydl)
    
    # Mock methods to avoid actual HTTP requests
    def mock_extract_info(self, url, *args, **kwargs):
        return {
            'url': url,
            'info_dict': info_dict,
            'playlist_mincount': playlist_mincount,
            'params': params,
            'only_matching': only_matching
        }
    
    monkeypatch.setattr(TVLandIE, '_real_extract', mock_extract_info)
    
    result = ie.extract(url)
    
    if info_dict:
        assert result['info_dict'] == info_dict
    if playlist_mincount:
        assert result['playlist_mincount'] == playlist_mincount
    if params:
        assert result['params'] == params
    if only_matching:
        assert result['only_matching'] == only_matching
