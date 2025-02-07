# file: youtube_dl/downloader/common.py:308-310
# asked: {"lines": [308, 310], "branches": []}
# gained: {"lines": [308, 310], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def to_screen(self, message):
        self.message = message

@pytest.fixture
def file_downloader():
    ydl = MockYDL()
    params = {}
    return FileDownloader(ydl, params)

def test_report_resuming_byte(file_downloader, mocker):
    mock_to_screen = mocker.patch.object(file_downloader, 'to_screen')
    resume_len = 1000
    file_downloader.report_resuming_byte(resume_len)
    mock_to_screen.assert_called_once_with('[download] Resuming download at byte %s' % resume_len)
