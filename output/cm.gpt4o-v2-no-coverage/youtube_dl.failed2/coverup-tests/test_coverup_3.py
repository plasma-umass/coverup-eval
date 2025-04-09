# file: youtube_dl/downloader/common.py:161-162
# asked: {"lines": [161, 162], "branches": []}
# gained: {"lines": [161, 162], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the FileDownloader class is defined in youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    @pytest.fixture
    def file_downloader(self):
        ydl = Mock()
        params = {}
        return FileDownloader(ydl, params)

    def test_report_warning(self, file_downloader):
        # Arrange
        warning_message = "This is a warning"
        
        # Act
        file_downloader.report_warning(warning_message)
        
        # Assert
        file_downloader.ydl.report_warning.assert_called_once_with(warning_message)
