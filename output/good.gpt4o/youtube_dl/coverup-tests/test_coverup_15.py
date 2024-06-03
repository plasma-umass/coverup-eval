# file youtube_dl/downloader/common.py:227-229
# lines [227, 229]
# branches []

import pytest
from unittest import mock
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def file_downloader(mocker):
    ydl = mocker.Mock()
    params = {}
    return FileDownloader(ydl, params)

def test_report_destination(file_downloader, mocker):
    mock_to_screen = mocker.patch.object(file_downloader, 'to_screen')
    filename = 'testfile.mp4'
    
    file_downloader.report_destination(filename)
    
    mock_to_screen.assert_called_once_with('[download] Destination: ' + filename)
