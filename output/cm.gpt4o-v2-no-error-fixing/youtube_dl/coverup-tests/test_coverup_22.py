# file: youtube_dl/downloader/fragment.py:17-19
# asked: {"lines": [19], "branches": []}
# gained: {"lines": [19], "branches": []}

import pytest
from youtube_dl.downloader.fragment import HttpQuietDownloader
from youtube_dl.downloader.http import HttpFD

def test_to_screen():
    downloader = HttpQuietDownloader(None, None)
    downloader.to_screen("test message")
    # No assertion needed as the method is a pass-through

def test_inheritance():
    downloader = HttpQuietDownloader(None, None)
    assert isinstance(downloader, HttpFD)
