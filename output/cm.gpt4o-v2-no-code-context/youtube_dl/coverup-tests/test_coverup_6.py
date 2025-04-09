# file: youtube_dl/downloader/common.py:368-370
# asked: {"lines": [368, 370], "branches": []}
# gained: {"lines": [368, 370], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

class DummyYDL:
    def __init__(self):
        self.params = {}

@pytest.fixture
def dummy_ydl():
    return DummyYDL()

def test_real_download_not_implemented(dummy_ydl):
    downloader = FileDownloader(dummy_ydl, dummy_ydl.params)
    with pytest.raises(NotImplementedError, match='This method must be implemented by subclasses'):
        downloader.real_download('dummy_filename', {'dummy_key': 'dummy_value'})
