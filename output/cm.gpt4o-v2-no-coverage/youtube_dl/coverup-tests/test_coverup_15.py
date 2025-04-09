# file: youtube_dl/downloader/common.py:158-159
# asked: {"lines": [159], "branches": []}
# gained: {"lines": [159], "branches": []}

import pytest
from unittest.mock import Mock
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    @pytest.fixture
    def file_downloader(self):
        ydl = Mock()
        params = {}
        return FileDownloader(ydl, params)

    def test_trouble(self, file_downloader):
        # Mock the ydl.trouble method
        file_downloader.ydl.trouble = Mock()

        # Call the trouble method with some arguments
        file_downloader.trouble('error', code=123)

        # Assert ydl.trouble was called with the same arguments
        file_downloader.ydl.trouble.assert_called_once_with('error', code=123)
