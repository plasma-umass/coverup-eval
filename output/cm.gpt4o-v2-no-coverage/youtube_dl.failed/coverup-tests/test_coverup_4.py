# file: youtube_dl/downloader/common.py:152-153
# asked: {"lines": [152, 153], "branches": []}
# gained: {"lines": [152, 153], "branches": []}

import pytest
from unittest.mock import Mock
from youtube_dl.downloader.common import FileDownloader

class TestFileDownloader:
    def test_to_stderr(self):
        ydl_mock = Mock()
        fd = FileDownloader(ydl_mock, {})
        
        test_message = "Test error message"
        fd.to_stderr(test_message)
        
        ydl_mock.to_screen.assert_called_once_with(test_message)
