# file youtube_dl/downloader/f4m.py:184-185
# lines [185]
# branches []

import pytest
from youtube_dl.downloader.f4m import FlvReader

class MockFlvReader:
    def __init__(self, bootstrap_bytes):
        self.bootstrap_bytes = bootstrap_bytes

    def read_bootstrap_info(self):
        return "mocked_bootstrap_info"

@pytest.fixture
def mock_flv_reader(mocker):
    mocker.patch('youtube_dl.downloader.f4m.FlvReader', MockFlvReader)

def test_read_bootstrap_info(mock_flv_reader):
    from youtube_dl.downloader.f4m import read_bootstrap_info

    bootstrap_bytes = b'some_fake_bootstrap_data'
    result = read_bootstrap_info(bootstrap_bytes)
    assert result == "mocked_bootstrap_info"
