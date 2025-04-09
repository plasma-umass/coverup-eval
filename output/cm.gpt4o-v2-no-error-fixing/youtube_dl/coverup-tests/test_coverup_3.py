# file: youtube_dl/downloader/ism.py:35-36
# asked: {"lines": [35, 36], "branches": []}
# gained: {"lines": [35, 36], "branches": []}

import pytest
from youtube_dl.downloader.ism import box
from youtube_dl.compat import compat_Struct

u32 = compat_Struct('>I')

def test_box():
    box_type = b'test'
    payload = b'data'
    result = box(box_type, payload)
    
    expected_length = u32.pack(8 + len(payload))
    expected_result = expected_length + box_type + payload
    
    assert result == expected_result
