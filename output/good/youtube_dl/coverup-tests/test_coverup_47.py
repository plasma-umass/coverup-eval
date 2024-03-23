# file youtube_dl/downloader/common.py:139-147
# lines [142, 143, 144, 145, 146, 147]
# branches ['143->144', '143->145']

import pytest
from youtube_dl.downloader.common import FileDownloader

@pytest.fixture
def cleanup():
    # Setup code if necessary
    yield
    # Cleanup code if necessary

def test_parse_bytes_with_unit(cleanup, mocker):
    # Test the parse_bytes method with a unit to cover lines 142-147
    assert FileDownloader.parse_bytes('1K') == 1024
    assert FileDownloader.parse_bytes('1M') == 1024**2
    assert FileDownloader.parse_bytes('1G') == 1024**3
    assert FileDownloader.parse_bytes('1T') == 1024**4
    assert FileDownloader.parse_bytes('1P') == 1024**5
    assert FileDownloader.parse_bytes('1E') == 1024**6
    assert FileDownloader.parse_bytes('1Z') == 1024**7
    assert FileDownloader.parse_bytes('1Y') == 1024**8
