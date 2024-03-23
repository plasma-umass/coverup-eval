# file youtube_dl/downloader/f4m.py:51-58
# lines [52, 53, 54, 55, 56, 57, 58]
# branches ['53->54', '55->56', '55->57']

import pytest
from youtube_dl.downloader.f4m import FlvReader

def test_flv_reader_read_string(mocker):
    # Mock the read_bytes method to return a string and then a null byte
    mocker.patch.object(FlvReader, 'read_bytes', side_effect=[b'a', b'b', b'\x00'])

    reader = FlvReader(b'')
    result = reader.read_string()

    # Assert that the result is the string before the null byte
    assert result == b'ab'

    # Assert that read_bytes was called three times
    assert FlvReader.read_bytes.call_count == 3

    # Cleanup is not necessary as we are using mocker.patch which is
    # automatically undone at the end of the test
