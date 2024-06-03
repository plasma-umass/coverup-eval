# file youtube_dl/downloader/common.py:325-327
# lines [325, 327]
# branches []

import pytest
from unittest import mock

# Assuming the FileDownloader class is imported from youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def to_screen(self, message):
        pass

def test_report_unable_to_resume(mocker):
    # Create a mock YDL object
    mock_ydl = MockYDL()
    
    # Create an instance of FileDownloader with mock arguments
    fd = FileDownloader(mock_ydl, {})
    
    # Mock the to_screen method
    mock_to_screen = mocker.patch.object(mock_ydl, 'to_screen')
    
    # Call the method to test
    fd.report_unable_to_resume()
    
    # Assert that to_screen was called with the correct argument
    mock_to_screen.assert_called_once_with('[download] Unable to resume')
