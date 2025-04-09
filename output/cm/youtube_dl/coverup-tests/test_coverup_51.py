# file youtube_dl/postprocessor/common.py:37-39
# lines [39]
# branches []

import pytest
from youtube_dl.postprocessor.common import PostProcessor

class MockDownloader:
    pass

@pytest.fixture
def mock_downloader():
    return MockDownloader()

def test_set_downloader_executes_line_39(mock_downloader):
    pp = PostProcessor()
    pp.set_downloader(mock_downloader)
    assert pp._downloader is mock_downloader, "Line 39 did not execute as expected"
