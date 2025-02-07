# file: youtube_dl/downloader/common.py:152-153
# asked: {"lines": [152, 153], "branches": []}
# gained: {"lines": [152, 153], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the FileDownloader class is defined in youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

def test_to_stderr():
    # Create a mock object for ydl with a to_screen method
    ydl_mock = Mock()
    ydl_mock.to_screen = Mock()

    # Create an instance of FileDownloader with the mock ydl
    fd = FileDownloader(ydl=ydl_mock, params={})

    # Call the to_stderr method with a test message
    test_message = "Test error message"
    fd.to_stderr(test_message)

    # Assert that ydl.to_screen was called with the test message
    ydl_mock.to_screen.assert_called_once_with(test_message)
