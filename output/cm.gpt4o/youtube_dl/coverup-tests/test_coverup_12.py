# file youtube_dl/downloader/fragment.py:61-62
# lines [61, 62]
# branches []

import pytest
from unittest import mock
from youtube_dl.downloader.fragment import FragmentFD

@pytest.fixture
def fragment_fd(mocker):
    params = {'quiet': True}
    fd = FragmentFD(mocker.Mock(), params)
    return fd

def test_report_skip_fragment(fragment_fd, mocker):
    mock_to_screen = mocker.patch.object(fragment_fd, 'to_screen')
    frag_index = 5
    fragment_fd.report_skip_fragment(frag_index)
    mock_to_screen.assert_called_once_with('[download] Skipping fragment %d...' % frag_index)
