# file: youtube_dl/downloader/common.py:227-229
# asked: {"lines": [227, 229], "branches": []}
# gained: {"lines": [227, 229], "branches": []}

import pytest
from unittest import mock

# Assuming the FileDownloader class is defined in youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def to_screen(self, message):
        pass

@pytest.fixture
def file_downloader():
    ydl = MockYDL()
    params = {}
    return FileDownloader(ydl, params)

def test_report_destination(file_downloader):
    with mock.patch.object(file_downloader, 'to_screen') as mock_to_screen:
        filename = 'testfile'
        file_downloader.report_destination(filename)
        mock_to_screen.assert_called_once_with('[download] Destination: ' + filename)
