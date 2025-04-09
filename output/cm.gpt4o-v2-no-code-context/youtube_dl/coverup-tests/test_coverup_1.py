# file: youtube_dl/downloader/common.py:227-229
# asked: {"lines": [227, 229], "branches": []}
# gained: {"lines": [227, 229], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockFileDownloader(FileDownloader):
    def __init__(self):
        self.screen_output = []

    def to_screen(self, message):
        self.screen_output.append(message)

@pytest.fixture
def mock_file_downloader():
    return MockFileDownloader()

def test_report_destination(mock_file_downloader):
    filename = 'testfile.txt'
    mock_file_downloader.report_destination(filename)
    assert '[download] Destination: testfile.txt' in mock_file_downloader.screen_output
