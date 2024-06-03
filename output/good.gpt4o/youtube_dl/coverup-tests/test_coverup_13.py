# file youtube_dl/downloader/common.py:164-165
# lines [164, 165]
# branches []

import pytest
from unittest import mock

# Assuming the FileDownloader class is imported from youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def report_error(self, *args, **kwargs):
        pass

@pytest.fixture
def file_downloader():
    ydl = MockYDL()
    params = {}
    fd = FileDownloader(ydl, params)
    return fd

def test_report_error(file_downloader, mocker):
    mock_report_error = mocker.patch.object(file_downloader.ydl, 'report_error')
    file_downloader.report_error('error message', code=404)
    mock_report_error.assert_called_once_with('error message', code=404)
