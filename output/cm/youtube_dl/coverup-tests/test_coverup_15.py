# file youtube_dl/downloader/common.py:227-229
# lines [227, 229]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockFileDownloader(FileDownloader):
    def __init__(self):
        self.screen_content = []

    def to_screen(self, message):
        self.screen_content.append(message)

@pytest.fixture
def mock_file_downloader():
    return MockFileDownloader()

def test_report_destination(mock_file_downloader):
    test_filename = 'test_video.mp4'
    mock_file_downloader.report_destination(test_filename)
    assert mock_file_downloader.screen_content == ['[download] Destination: test_video.mp4']
