# file youtube_dl/downloader/f4m.py:72-91
# lines [74, 76, 77, 79, 80, 82, 83, 84, 85, 86, 87, 89, 90]
# branches ['79->80', '79->82', '84->85', '84->89']

import pytest
from youtube_dl.downloader.f4m import FlvReader

class TestFlvReader:
    def test_read_asrt(self, mocker):
        # Mock the data to be read by FlvReader
        data = b'\x00'  # version
        data += b'\x00\x00\x00'  # flags
        data += b'\x01'  # quality_entry_count
        data += b'\x00\x04test'  # quality_entry
        data += b'\x00\x00\x00\x01'  # segment_run_count
        data += b'\x00\x00\x00\x01'  # first_segment
        data += b'\x00\x00\x00\x02'  # fragments_per_segment

        # Mock the methods used in read_asrt that are not under test
        mocker.patch.object(FlvReader, 'read_unsigned_char', side_effect=[1, 4])
        mocker.patch.object(FlvReader, 'read_bytes', return_value=b'\x00\x00\x00')
        mocker.patch.object(FlvReader, 'read_unsigned_int', side_effect=[1, 1, 2])
        mocker.patch.object(FlvReader, 'read_string', return_value='test')

        reader = FlvReader(data)
        result = reader.read_asrt()

        # Assertions to verify postconditions
        assert result == {'segment_run': [(1, 2)]}

        # Clean up
        reader.close()
