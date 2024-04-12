# file youtube_dl/downloader/fragment.py:252-279
# lines [253, 254, 255, 256, 257, 258, 260, 261, 263, 264, 265, 266, 267, 268, 269, 270, 271, 273, 274, 275, 276, 277, 278]
# branches ['254->255', '254->258', '256->257', '256->258', '260->261', '260->263', '264->265', '264->271', '266->267', '266->271']

import os
import time
from unittest.mock import Mock
import pytest

from youtube_dl.downloader.fragment import FragmentFD

@pytest.fixture
def mock_fragment_downloader(tmp_path):
    ydl_mock = Mock()
    ydl_mock.params = {'verbose': False}
    fd = FragmentFD(ydl_mock, {'updatetime': True})
    fd.ytdl_filename = lambda _: str(tmp_path / "ytdl_file.tmp")
    fd.report_error = Mock()
    fd.report_warning = Mock()
    fd.report_retry = Mock()
    fd.report_file_already_downloaded = Mock()
    fd.report_file_delete = Mock()
    fd.try_rename = Mock()
    fd._hook_progress = Mock()
    return fd

def test_finish_frag_download(mock_fragment_downloader, tmp_path):
    ctx = {
        'dest_stream': Mock(),
        'filename': str(tmp_path / "test_video.mp4"),
        'tmpfilename': str(tmp_path / "test_video.part"),
        'started': time.time() - 5,
        'complete_frags_downloaded_bytes': 1024,
        'fragment_filetime': time.time() - 1000,
        'live': False  # Add 'live' key to ctx to avoid KeyError
    }

    # Create the temporary file to simulate a download
    with open(ctx['tmpfilename'], 'wb') as f:
        f.write(os.urandom(1024))

    # Simulate renaming the temporary file to the final filename
    mock_fragment_downloader.try_rename.side_effect = lambda src, dst: os.rename(src, dst)

    mock_fragment_downloader._finish_frag_download(ctx)

    # Assertions to check postconditions
    ctx['dest_stream'].close.assert_called_once()
    mock_fragment_downloader.try_rename.assert_called_once_with(ctx['tmpfilename'], ctx['filename'])
    assert os.path.isfile(ctx['filename'])
    assert not os.path.isfile(ctx['tmpfilename'])
    assert ctx['complete_frags_downloaded_bytes'] == os.path.getsize(ctx['filename'])
    mock_fragment_downloader._hook_progress.assert_called_once()

    # Clean up
    os.remove(ctx['filename'])
