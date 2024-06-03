# file youtube_dl/downloader/common.py:122-124
# lines [124]
# branches []

import pytest
from youtube_dl.downloader.common import FileDownloader

def test_format_retries_inf():
    assert FileDownloader.format_retries(float('inf')) == 'inf'

def test_format_retries_number():
    assert FileDownloader.format_retries(5) == '5'
    assert FileDownloader.format_retries(0) == '0'
    assert FileDownloader.format_retries(3.5) == '4'
