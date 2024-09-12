# file: youtube_dl/downloader/common.py:376-379
# asked: {"lines": [376, 379], "branches": []}
# gained: {"lines": [376, 379], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

def test_add_progress_hook():
    ydl = None  # Mock or create a suitable YoutubeDL object if necessary
    params = {}
    fd = FileDownloader(ydl, params)
    
    def mock_hook(status):
        pass
    
    fd.add_progress_hook(mock_hook)
    
    assert mock_hook in fd._progress_hooks

    # Clean up
    fd._progress_hooks.remove(mock_hook)
    assert mock_hook not in fd._progress_hooks
