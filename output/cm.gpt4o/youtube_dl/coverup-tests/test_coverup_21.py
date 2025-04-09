# file youtube_dl/downloader/fragment.py:72-74
# lines [74]
# branches []

import pytest
from youtube_dl.downloader.fragment import FragmentFD

def test_do_ytdl_file():
    ctx_live = {'live': True, 'tmpfilename': 'testfile'}
    ctx_tmpfilename_dash = {'live': False, 'tmpfilename': '-'}
    ctx_normal = {'live': False, 'tmpfilename': 'testfile'}

    assert not FragmentFD._FragmentFD__do_ytdl_file(ctx_live)
    assert not FragmentFD._FragmentFD__do_ytdl_file(ctx_tmpfilename_dash)
    assert FragmentFD._FragmentFD__do_ytdl_file(ctx_normal)
