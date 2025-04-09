# file: youtube_dl/downloader/fragment.py:61-62
# asked: {"lines": [61, 62], "branches": []}
# gained: {"lines": [61, 62], "branches": []}

import pytest
from youtube_dl.downloader.fragment import FragmentFD
from unittest.mock import patch, MagicMock

@pytest.fixture
def fragment_fd():
    ydl = MagicMock()
    params = {}
    return FragmentFD(ydl, params)

def test_report_skip_fragment(fragment_fd):
    with patch.object(fragment_fd, 'to_screen') as mock_to_screen:
        fragment_fd.report_skip_fragment(5)
        mock_to_screen.assert_called_once_with('[download] Skipping fragment %d...' % 5)
