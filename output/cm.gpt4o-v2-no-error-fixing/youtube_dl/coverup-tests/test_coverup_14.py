# file: youtube_dl/downloader/common.py:325-327
# asked: {"lines": [327], "branches": []}
# gained: {"lines": [327], "branches": []}

import pytest
from unittest import mock
from youtube_dl.downloader.common import FileDownloader

def test_report_unable_to_resume():
    ydl = mock.Mock()
    fd = FileDownloader(ydl, {})
    
    with mock.patch.object(fd, 'to_screen') as mock_to_screen:
        fd.report_unable_to_resume()
        mock_to_screen.assert_called_once_with('[download] Unable to resume')
