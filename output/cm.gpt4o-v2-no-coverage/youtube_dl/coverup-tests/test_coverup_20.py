# file: youtube_dl/downloader/fragment.py:72-74
# asked: {"lines": [74], "branches": []}
# gained: {"lines": [74], "branches": []}

import pytest
from youtube_dl.downloader.fragment import FragmentFD

def test_do_ytdl_file_live():
    ctx = {'live': True, 'tmpfilename': 'testfile'}
    result = FragmentFD._FragmentFD__do_ytdl_file(ctx)
    assert result is False

def test_do_ytdl_file_tmpfilename_dash():
    ctx = {'live': False, 'tmpfilename': '-'}
    result = FragmentFD._FragmentFD__do_ytdl_file(ctx)
    assert result is False

def test_do_ytdl_file_valid():
    ctx = {'live': False, 'tmpfilename': 'testfile'}
    result = FragmentFD._FragmentFD__do_ytdl_file(ctx)
    assert result is True
