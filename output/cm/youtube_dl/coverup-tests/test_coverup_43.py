# file youtube_dl/downloader/fragment.py:98-113
# lines [99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113]
# branches ['105->106', '105->107', '107->108', '107->109']

import os
import pytest
from youtube_dl.downloader.fragment import FragmentFD

class MockDownloader:
    def __init__(self, params):
        pass

    def download(self, filename, info_dict):
        with open(filename, 'wb') as f:
            f.write(b'test data')
        return True

@pytest.fixture
def mock_downloader(mocker):
    mocker.patch('youtube_dl.downloader.fragment.FileDownloader', MockDownloader)

def test_download_fragment_success(mock_downloader, tmp_path):
    fragment_fd = FragmentFD(None, {})
    ctx = {
        'tmpfilename': str(tmp_path / 'test'),
        'fragment_index': 1,
        'dl': MockDownloader({}),
    }
    frag_url = 'http://example.com/frag1'
    info_dict = {}

    success, frag_content = fragment_fd._download_fragment(ctx, frag_url, info_dict)

    assert success is True
    assert frag_content == b'test data'
    assert ctx['fragment_filename_sanitized'] == str(tmp_path / 'test-Frag1')
    assert os.path.isfile(ctx['fragment_filename_sanitized'])
    os.remove(ctx['fragment_filename_sanitized'])
