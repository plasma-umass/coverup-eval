# file youtube_dl/downloader/common.py:376-379
# lines [376, 379]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def file_downloader(mocker):
    ydl = mocker.Mock()
    params = {}
    fd = FileDownloader(ydl, params)
    fd._progress_hooks = []
    return fd

def test_add_progress_hook(file_downloader):
    def mock_progress_hook(d):
        pass

    file_downloader.add_progress_hook(mock_progress_hook)
    
    assert len(file_downloader._progress_hooks) == 1
    assert file_downloader._progress_hooks[0] == mock_progress_hook
