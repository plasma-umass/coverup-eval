# file: youtube_dl/downloader/common.py:155-156
# asked: {"lines": [155, 156], "branches": []}
# gained: {"lines": [155, 156], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming FileDownloader is defined in youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def to_console_title(self, message):
        pass

@pytest.fixture
def file_downloader():
    ydl = MockYDL()
    params = {}
    return FileDownloader(ydl, params)

def test_to_console_title(file_downloader):
    mock_message = "Test Message"
    file_downloader.ydl.to_console_title = Mock()
    
    file_downloader.to_console_title(mock_message)
    
    file_downloader.ydl.to_console_title.assert_called_once_with(mock_message)
