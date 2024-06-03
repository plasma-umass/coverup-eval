# file youtube_dl/downloader/common.py:195-196
# lines [195, 196]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def __init__(self):
        self.params = {}

def test_ytdl_filename():
    ydl = MockYDL()
    params = {}
    fd = FileDownloader(ydl, params)
    filename = "testfile"
    expected = "testfile.ytdl"
    result = fd.ytdl_filename(filename)
    assert result == expected, f"Expected {expected}, but got {result}"
