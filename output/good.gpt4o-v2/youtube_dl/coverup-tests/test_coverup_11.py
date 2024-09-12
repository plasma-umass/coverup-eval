# file: youtube_dl/downloader/common.py:325-327
# asked: {"lines": [325, 327], "branches": []}
# gained: {"lines": [325, 327], "branches": []}

import pytest
from unittest.mock import Mock

# Assuming the FileDownloader class is defined in the module youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

def test_report_unable_to_resume():
    # Create a mock for the ydl object with a to_screen method
    ydl_mock = Mock()
    ydl_mock.to_screen = Mock()

    # Create an instance of FileDownloader with the mock ydl object
    fd = FileDownloader(ydl_mock, {})

    # Call the report_unable_to_resume method
    fd.report_unable_to_resume()

    # Assert that the to_screen method was called with the expected message
    ydl_mock.to_screen.assert_called_once_with('[download] Unable to resume')
