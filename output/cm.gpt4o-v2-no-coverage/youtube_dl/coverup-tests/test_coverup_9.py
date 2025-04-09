# file: youtube_dl/downloader/common.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import Mock
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    @pytest.fixture
    def file_downloader(self):
        ydl = Mock()
        params = {}
        return FileDownloader(ydl, params)

    def test_report_warning(self, file_downloader):
        file_downloader.report_warning("This is a warning")
        file_downloader.ydl.report_warning.assert_called_once_with("This is a warning")
