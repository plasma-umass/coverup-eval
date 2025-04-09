# file youtube_dl/downloader/common.py:368-370
# lines [368, 370]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

class MockYDL:
    def __init__(self):
        self.params = {}

def test_real_download_not_implemented():
    ydl = MockYDL()
    params = {}
    downloader = FileDownloader(ydl, params)
    with pytest.raises(NotImplementedError) as excinfo:
        downloader.real_download('dummy_filename', {})
    assert str(excinfo.value) == 'This method must be implemented by subclasses'
