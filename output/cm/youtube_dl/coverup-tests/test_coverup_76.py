# file youtube_dl/downloader/fragment.py:17-19
# lines [19]
# branches []

import pytest
from youtube_dl.downloader.fragment import HttpQuietDownloader
from youtube_dl.downloader.common import FileDownloader

def test_HttpQuietDownloader_to_screen(mocker):
    # Mock the FileDownloader.__init__ to not require params
    mocker.patch.object(FileDownloader, '__init__', return_value=None)

    # Instantiate the HttpQuietDownloader
    downloader = HttpQuietDownloader(None)

    # Call the to_screen method
    downloader.to_screen("test message")

    # Since to_screen is a pass-through (no-op), we don't have any direct postconditions to assert.
    # The test is simply to ensure that calling the method does not raise an error.
