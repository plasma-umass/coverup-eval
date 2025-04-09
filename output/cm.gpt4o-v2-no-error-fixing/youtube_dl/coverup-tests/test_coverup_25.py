# file: youtube_dl/downloader/common.py:227-229
# asked: {"lines": [229], "branches": []}
# gained: {"lines": [229], "branches": []}

import pytest
from unittest import mock
from youtube_dl.downloader.common import FileDownloader

def test_report_destination(monkeypatch):
    # Arrange
    ydl = mock.Mock()
    params = {}
    fd = FileDownloader(ydl, params)
    filename = "testfile.txt"
    
    # Mock the to_screen method to verify it is called with the correct argument
    to_screen_mock = mock.Mock()
    monkeypatch.setattr(fd, 'to_screen', to_screen_mock)
    
    # Act
    fd.report_destination(filename)
    
    # Assert
    to_screen_mock.assert_called_once_with('[download] Destination: ' + filename)
