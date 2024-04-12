# file youtube_dl/downloader/common.py:376-379
# lines [376, 379]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockDownloader(FileDownloader):
    def __init__(self):
        self._progress_hooks = []

def test_add_progress_hook():
    # Setup
    fd = MockDownloader()

    # Define a dummy progress hook function
    def dummy_progress_hook(status):
        pass

    # Test adding a progress hook
    fd.add_progress_hook(dummy_progress_hook)

    # Assert that the progress hook was added
    assert dummy_progress_hook in fd._progress_hooks
