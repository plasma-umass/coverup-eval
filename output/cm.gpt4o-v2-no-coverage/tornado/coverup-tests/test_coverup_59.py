# file: tornado/util.py:441-454
# asked: {"lines": [441, 450, 451, 452, 453, 454], "branches": [[452, 453], [452, 454]]}
# gained: {"lines": [441, 450, 451, 452, 453, 454], "branches": [[452, 453], [452, 454]]}

import pytest
from tornado.util import _websocket_mask_python

def test_websocket_mask_python():
    mask = b'\x01\x02\x03\x04'
    data = b'\x10\x20\x30\x40\x50'
    expected_output = b'\x11\x22\x33\x44\x51'
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output

    # Test with empty data
    data = b''
    expected_output = b''
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output

    # Test with data length less than mask length
    data = b'\x10\x20'
    expected_output = b'\x11\x22'
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output

    # Test with data length equal to mask length
    data = b'\x10\x20\x30\x40'
    expected_output = b'\x11\x22\x33\x44'
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output

    # Test with data length greater than mask length
    data = b'\x10\x20\x30\x40\x50\x60'
    expected_output = b'\x11\x22\x33\x44\x51\x62'
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output
