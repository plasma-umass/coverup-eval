# file youtube_dl/postprocessor/common.py:37-39
# lines [39]
# branches []

import pytest
from youtube_dl.postprocessor.common import PostProcessor

def test_set_downloader():
    class MockDownloader:
        pass

    pp = PostProcessor()
    downloader = MockDownloader()
    
    pp.set_downloader(downloader)
    
    assert pp._downloader is downloader
