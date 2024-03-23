# file youtube_dl/downloader/common.py:308-310
# lines [308, 310]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockFileDownloader(FileDownloader):
    def __init__(self, ydl, params):
        super().__init__(ydl, params)
        self.params = params

    def to_screen(self, message):
        self.last_screen_message = message

@pytest.fixture
def mock_file_downloader(mocker):
    ydl_mock = mocker.MagicMock()
    return MockFileDownloader(ydl_mock, params={})

def test_report_resuming_byte(mock_file_downloader):
    resume_len = 1000
    mock_file_downloader.report_resuming_byte(resume_len)
    expected_message = '[download] Resuming download at byte 1000'
    assert mock_file_downloader.last_screen_message == expected_message
