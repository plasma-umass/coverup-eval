# file: youtube_dl/downloader/common.py:155-156
# asked: {"lines": [155, 156], "branches": []}
# gained: {"lines": [155, 156], "branches": []}

import pytest
from unittest.mock import Mock
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    @pytest.fixture
    def file_downloader(self):
        ydl = Mock()
        params = {}
        return FileDownloader(ydl, params)

    def test_to_console_title(self, file_downloader):
        message = "Test Message"
        file_downloader.to_console_title(message)
        file_downloader.ydl.to_console_title.assert_called_once_with(message)
