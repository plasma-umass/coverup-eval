# file: youtube_dl/downloader/ism.py:35-36
# asked: {"lines": [35, 36], "branches": []}
# gained: {"lines": [35], "branches": []}

import pytest
import struct
from youtube_dl.compat import compat_Struct

u32 = compat_Struct('>I')

def box(box_type, payload):
    return u32.pack(8 + len(payload)) + box_type + payload

def test_box():
    box_type = b'test'
    payload = b'data'
    expected_length = 8 + len(payload)
    expected_output = struct.pack('>I', expected_length) + box_type + payload

    result = box(box_type, payload)
    
    assert result == expected_output
