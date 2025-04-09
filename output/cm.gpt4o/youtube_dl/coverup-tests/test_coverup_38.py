# file youtube_dl/extractor/nrk.py:830-844
# lines [843, 844]
# branches []

import pytest
from youtube_dl.extractor.nrk import NRKTVEpisodesIE
from youtube_dl.YoutubeDL import YoutubeDL

@pytest.fixture
def mock_webpage():
    return '''
    <html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Test Title</h1>
            <div>Some content here</div>
        </body>
    </html>
    '''

@pytest.fixture
def mock_downloader(mocker):
    downloader = mocker.Mock(spec=YoutubeDL)
    downloader.params = {'no_color': True}
    return downloader

def test_extract_title(mock_webpage, mock_downloader, mocker):
    ie = NRKTVEpisodesIE(downloader=mock_downloader)
    mocker.patch.object(ie, '_html_search_regex', wraps=ie._html_search_regex)
    
    title = ie._extract_title(mock_webpage)
    
    ie._html_search_regex.assert_called_once_with(
        r'<h1>([^<]+)</h1>', mock_webpage, 'title', fatal=False)
    assert title == 'Test Title'
