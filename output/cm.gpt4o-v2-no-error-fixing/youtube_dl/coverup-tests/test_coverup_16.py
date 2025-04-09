# file: youtube_dl/downloader/f4m.py:210-211
# asked: {"lines": [211], "branches": []}
# gained: {"lines": [211], "branches": []}

import io
from youtube_dl.downloader.f4m import write_unsigned_int

def test_write_unsigned_int():
    stream = io.BytesIO()
    write_unsigned_int(stream, 42)
    stream.seek(0)
    result = stream.read()
    assert result == b'\x00\x00\x00*'
