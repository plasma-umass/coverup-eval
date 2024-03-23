# file youtube_dl/downloader/fragment.py:61-62
# lines [61, 62]
# branches []

import pytest
from youtube_dl.downloader.fragment import FragmentFD

class MockFileDownloader(FragmentFD):
    def to_screen(self, message):
        self.logged_message = message

@pytest.fixture
def mock_fragment_downloader():
    return MockFileDownloader(None, None)

def test_report_skip_fragment(mock_fragment_downloader):
    frag_index = 5
    mock_fragment_downloader.report_skip_fragment(frag_index)
    expected_message = '[download] Skipping fragment 5...'
    assert mock_fragment_downloader.logged_message == expected_message
