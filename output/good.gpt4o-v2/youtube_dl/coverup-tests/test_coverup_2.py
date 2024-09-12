# file: youtube_dl/downloader/common.py:195-196
# asked: {"lines": [195, 196], "branches": []}
# gained: {"lines": [195, 196], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

def test_ytdl_filename():
    fd = FileDownloader(None, None)
    filename = "testfile"
    expected = "testfile.ytdl"
    result = fd.ytdl_filename(filename)
    assert result == expected, f"Expected {expected}, but got {result}"
