# file youtube_dl/downloader/common.py:161-162
# lines [161, 162]
# branches []

import pytest
from unittest import mock

# Assuming the FileDownloader class is imported from youtube_dl.downloader.common
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def report_warning(self, *args, **kwargs):
        pass

@pytest.fixture
def file_downloader():
    ydl = MockYDL()
    params = {}
    fd = FileDownloader(ydl, params)
    return fd

def test_report_warning(file_downloader, mocker):
    mock_report_warning = mocker.patch.object(file_downloader.ydl, 'report_warning')
    file_downloader.report_warning('Test warning', some_kwarg='value')
    mock_report_warning.assert_called_once_with('Test warning', some_kwarg='value')
