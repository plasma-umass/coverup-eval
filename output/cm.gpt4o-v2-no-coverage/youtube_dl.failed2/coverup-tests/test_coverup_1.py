# file: youtube_dl/downloader/f4m.py:93-125
# asked: {"lines": [93, 95, 97, 99, 101, 103, 104, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120, 123, 124], "branches": [[103, 104], [103, 106], [108, 109], [108, 123], [112, 113], [112, 115]]}
# gained: {"lines": [93], "branches": []}

import io
import pytest
from youtube_dl.compat import compat_struct_unpack

class FlvReader(io.BytesIO):
    def read_unsigned_char(self):
        return compat_struct_unpack('!B', self.read_bytes(1))[0]

    def read_bytes(self, n):
        data = self.read(n)
        if len(data) < n:
            raise DataTruncatedError('FlvReader error: need %d bytes while only %d bytes got' % (n, len(data)))
        return data

    def read_unsigned_int(self):
        return compat_struct_unpack('!I', self.read_bytes(4))[0]

    def read_string(self):
        res = b''
        while True:
            char = self.read_bytes(1)
            if char == b'\x00':
                break
            res += char
        return res

    def read_unsigned_long_long(self):
        return compat_struct_unpack('!Q', self.read_bytes(8))[0]

    def read_afrt(self):
        # version
        self.read_unsigned_char()
        # flags
        self.read_bytes(3)
        # time scale
        self.read_unsigned_int()

        quality_entry_count = self.read_unsigned_char()
        # QualitySegmentUrlModifiers
        for i in range(quality_entry_count):
            self.read_string()

        fragments_count = self.read_unsigned_int()
        fragments = []
        for i in range(fragments_count):
            first = self.read_unsigned_int()
            first_ts = self.read_unsigned_long_long()
            duration = self.read_unsigned_int()
            if duration == 0:
                discontinuity_indicator = self.read_unsigned_char()
            else:
                discontinuity_indicator = None
            fragments.append({
                'first': first,
                'ts': first_ts,
                'duration': duration,
                'discontinuity_indicator': discontinuity_indicator,
            })

        return {
            'fragments': fragments,
        }

def test_read_afrt_with_no_fragments():
    data = (
        b'\x01'  # version
        b'\x00\x00\x00'  # flags
        b'\x00\x00\x00\x01'  # time scale
        b'\x00'  # quality_entry_count
        b'\x00\x00\x00\x00'  # fragments_count
    )
    reader = FlvReader(data)
    result = reader.read_afrt()
    assert result == {'fragments': []}

def test_read_afrt_with_fragments():
    data = (
        b'\x01'  # version
        b'\x00\x00\x00'  # flags
        b'\x00\x00\x00\x01'  # time scale
        b'\x00'  # quality_entry_count
        b'\x00\x00\x00\x02'  # fragments_count
        b'\x00\x00\x00\x01'  # first
        b'\x00\x00\x00\x00\x00\x00\x00\x01'  # first_ts
        b'\x00\x00\x00\x05'  # duration
        b'\x00\x00\x00\x02'  # first
        b'\x00\x00\x00\x00\x00\x00\x00\x02'  # first_ts
        b'\x00\x00\x00\x00'  # duration
        b'\x01'  # discontinuity_indicator
    )
    reader = FlvReader(data)
    result = reader.read_afrt()
    assert result == {
        'fragments': [
            {'first': 1, 'ts': 1, 'duration': 5, 'discontinuity_indicator': None},
            {'first': 2, 'ts': 2, 'duration': 0, 'discontinuity_indicator': 1},
        ]
    }
