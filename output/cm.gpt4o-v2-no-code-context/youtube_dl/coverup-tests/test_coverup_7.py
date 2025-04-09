# file: youtube_dl/downloader/common.py:376-379
# asked: {"lines": [376, 379], "branches": []}
# gained: {"lines": [376, 379], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def file_downloader(mocker):
    ydl_mock = mocker.Mock()
    params_mock = mocker.Mock()
    return FileDownloader(ydl_mock, params_mock)

def test_add_progress_hook(file_downloader, mocker):
    mock_hook = mocker.Mock()
    file_downloader._progress_hooks = []
    
    file_downloader.add_progress_hook(mock_hook)
    
    assert mock_hook in file_downloader._progress_hooks
