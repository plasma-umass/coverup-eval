# file: tornado/util.py:441-454
# asked: {"lines": [441, 450, 451, 452, 453, 454], "branches": [[452, 453], [452, 454]]}
# gained: {"lines": [441, 450, 451, 452, 453, 454], "branches": [[452, 453], [452, 454]]}

import pytest
from tornado.util import _websocket_mask_python

def test_websocket_mask_python():
    mask = bytes([0x01, 0x02, 0x03, 0x04])
    data = bytes([0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11])
    expected_output = bytes([0x0b, 0x09, 0x0f, 0x09, 0x0f, 0x0d, 0x13, 0x15])
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output

