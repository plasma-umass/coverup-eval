# file: youtube_dl/downloader/fragment.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from youtube_dl.downloader.fragment import FragmentFD
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def to_screen(self, message):
        self.message = message

@pytest.fixture
def mock_ydl():
    return MockYDL()

@pytest.fixture
def fragment_fd(mock_ydl):
    return FragmentFD(mock_ydl, {})

def test_report_skip_fragment(fragment_fd, mock_ydl):
    frag_index = 5
    fragment_fd.report_skip_fragment(frag_index)
    assert mock_ydl.message == '[download] Skipping fragment %d...' % frag_index
