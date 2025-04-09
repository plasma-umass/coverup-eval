# file youtube_dl/downloader/fragment.py:72-74
# lines [74]
# branches []

import pytest
from youtube_dl.downloader.fragment import FragmentFD

def test_do_ytdl_file_non_live_non_dash():
    # Setup the context with 'live' as False and 'tmpfilename' not equal to '-'
    ctx = {'live': False, 'tmpfilename': 'testfile.tmp'}

    # Call the static method directly to test it
    result = FragmentFD._FragmentFD__do_ytdl_file(ctx)

    # Assert that the result is True, which means the line 74 was executed
    assert result == True

def test_do_ytdl_file_live():
    # Setup the context with 'live' as True
    ctx = {'live': True, 'tmpfilename': 'testfile.tmp'}

    # Call the static method directly to test it
    result = FragmentFD._FragmentFD__do_ytdl_file(ctx)

    # Assert that the result is False, which means the line 74 was executed
    assert result == False

def test_do_ytdl_file_dash():
    # Setup the context with 'tmpfilename' equal to '-'
    ctx = {'live': False, 'tmpfilename': '-'}

    # Call the static method directly to test it
    result = FragmentFD._FragmentFD__do_ytdl_file(ctx)

    # Assert that the result is False, which means the line 74 was executed
    assert result == False
