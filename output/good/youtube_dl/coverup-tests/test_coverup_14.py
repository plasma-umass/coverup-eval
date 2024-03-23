# file youtube_dl/downloader/common.py:325-327
# lines [325, 327]
# branches []

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

def test_report_unable_to_resume(mock_file_downloader):
    mock_file_downloader.report_unable_to_resume()
    assert '[download] Unable to resume' in mock_file_downloader.screen_output
