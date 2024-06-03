# file youtube_dl/downloader/common.py:308-310
# lines [308, 310]
# branches []

import pytest
from unittest import mock

# Assuming the FileDownloader class is imported from youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def file_downloader(mocker):
    # Mock the ydl and params arguments required by FileDownloader
    ydl = mocker.Mock()
    params = {}
    return FileDownloader(ydl, params)

def test_report_resuming_byte(file_downloader, mocker):
    # Mock the to_screen method
    mock_to_screen = mocker.patch.object(file_downloader, 'to_screen')

    # Call the method with a test value
    resume_len = 1024
    file_downloader.report_resuming_byte(resume_len)

    # Assert that to_screen was called with the correct message
    mock_to_screen.assert_called_once_with('[download] Resuming download at byte %s' % resume_len)
