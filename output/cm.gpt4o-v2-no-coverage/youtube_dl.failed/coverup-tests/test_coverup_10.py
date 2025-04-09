# file: youtube_dl/downloader/common.py:368-370
# asked: {"lines": [368, 370], "branches": []}
# gained: {"lines": [368, 370], "branches": []}

import pytest
from youtube_dl.downloader.common import FileDownloader

def test_real_download_not_implemented():
    fd = FileDownloader(ydl=None, params={})
    with pytest.raises(NotImplementedError, match="This method must be implemented by subclasses"):
        fd.real_download("dummy_filename", {"dummy_key": "dummy_value"})
