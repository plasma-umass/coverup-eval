# file: youtube_dl/downloader/common.py:325-327
# asked: {"lines": [325, 327], "branches": []}
# gained: {"lines": [325, 327], "branches": []}

import pytest
from unittest.mock import MagicMock
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def file_downloader():
    ydl = MagicMock()
    params = {}
    return FileDownloader(ydl, params)

def test_report_unable_to_resume(file_downloader):
    file_downloader.to_screen = MagicMock()
    file_downloader.report_unable_to_resume()
    file_downloader.to_screen.assert_called_once_with('[download] Unable to resume')
