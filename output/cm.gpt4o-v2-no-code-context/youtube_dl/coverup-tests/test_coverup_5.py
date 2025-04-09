# file: youtube_dl/downloader/common.py:195-196
# asked: {"lines": [195, 196], "branches": []}
# gained: {"lines": [195, 196], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def __init__(self):
        self.params = {}

@pytest.fixture
def file_downloader():
    ydl = MockYDL()
    params = {}
    return FileDownloader(ydl, params)

def test_ytdl_filename(file_downloader):
    filename = "testfile"
    expected_result = "testfile.ytdl"
    result = file_downloader.ytdl_filename(filename)
    assert result == expected_result
