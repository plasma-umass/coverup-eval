# file: youtube_dl/downloader/common.py:164-165
# asked: {"lines": [164, 165], "branches": []}
# gained: {"lines": [164, 165], "branches": []}

import pytest
from unittest.mock import Mock
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    @pytest.fixture
    def file_downloader(self):
        ydl = Mock()
        params = {}
        return FileDownloader(ydl, params)

    def test_report_error(self, file_downloader):
        # Arrange
        file_downloader.ydl.report_error = Mock()

        # Act
        file_downloader.report_error('error message')

        # Assert
        file_downloader.ydl.report_error.assert_called_once_with('error message')
