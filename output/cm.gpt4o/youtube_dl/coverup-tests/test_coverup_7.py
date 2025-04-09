# file youtube_dl/downloader/common.py:155-156
# lines [155, 156]
# branches []

import pytest
from unittest import mock

# Assuming the FileDownloader class is imported from youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def to_console_title(self, message):
        pass

@pytest.fixture
def file_downloader():
    ydl = MockYDL()
    params = {}
    fd = FileDownloader(ydl, params)
    return fd

def test_to_console_title(file_downloader, mocker):
    mock_to_console_title = mocker.patch.object(file_downloader.ydl, 'to_console_title')
    message = "Test Message"
    
    file_downloader.to_console_title(message)
    
    mock_to_console_title.assert_called_once_with(message)
