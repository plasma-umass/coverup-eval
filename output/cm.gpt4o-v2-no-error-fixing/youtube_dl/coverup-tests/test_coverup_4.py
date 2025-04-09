# file: youtube_dl/downloader/fragment.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from youtube_dl.downloader.fragment import FragmentFD
from youtube_dl.downloader.common import FileDownloader

class MockFileDownloader(FileDownloader):
    def __init__(self, ydl, params):
        super().__init__(ydl, params)
        self.screen_output = []

    def to_screen(self, *args, **kargs):
        self.screen_output.append(args[0])

@pytest.fixture
def mock_file_downloader():
    return MockFileDownloader(None, {})

def test_report_skip_fragment(mock_file_downloader):
    fragment_fd = FragmentFD(None, {})
    fragment_fd.to_screen = mock_file_downloader.to_screen
    fragment_fd.report_skip_fragment(5)
    assert mock_file_downloader.screen_output == ['[download] Skipping fragment 5...']
