# file: youtube_dl/postprocessor/common.py:34-35
# asked: {"lines": [35], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest
from youtube_dl.postprocessor.common import PostProcessor

def test_postprocessor_init_with_downloader():
    downloader_mock = object()  # Using a simple object as a mock
    pp = PostProcessor(downloader=downloader_mock)
    assert pp._downloader is downloader_mock

def test_postprocessor_init_without_downloader():
    pp = PostProcessor()
    assert pp._downloader is None
