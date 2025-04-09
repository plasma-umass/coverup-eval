# file: youtube_dl/postprocessor/common.py:37-39
# asked: {"lines": [39], "branches": []}
# gained: {"lines": [39], "branches": []}

import pytest
from youtube_dl.postprocessor.common import PostProcessor

def test_set_downloader():
    pp = PostProcessor()
    downloader_mock = object()
    
    pp.set_downloader(downloader_mock)
    
    assert pp._downloader is downloader_mock
