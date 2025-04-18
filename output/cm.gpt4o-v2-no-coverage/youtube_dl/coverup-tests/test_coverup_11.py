# file: youtube_dl/downloader/common.py:149-150
# asked: {"lines": [149, 150], "branches": []}
# gained: {"lines": [149, 150], "branches": []}

import pytest
from unittest.mock import Mock
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    @pytest.fixture
    def file_downloader(self):
        ydl_mock = Mock()
        params = {}
        return FileDownloader(ydl_mock, params)

    def test_to_screen(self, file_downloader):
        file_downloader.to_screen("Test message")
        file_downloader.ydl.to_screen.assert_called_once_with("Test message")
