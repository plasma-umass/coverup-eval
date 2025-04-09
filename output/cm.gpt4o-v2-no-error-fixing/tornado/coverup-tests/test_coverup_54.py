# file: tornado/util.py:441-454
# asked: {"lines": [441, 450, 451, 452, 453, 454], "branches": [[452, 453], [452, 454]]}
# gained: {"lines": [441, 450, 451, 452, 453, 454], "branches": [[452, 453], [452, 454]]}

import pytest
from tornado.util import _websocket_mask_python

def test_websocket_mask_python():
    mask = b'\x01\x02\x03\x04'
    data = b'\x10\x20\x30\x40'
    expected_output = b'\x11\x22\x33\x44'
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output

def test_websocket_mask_python_empty_data():
    mask = b'\x01\x02\x03\x04'
    data = b''
    expected_output = b''
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output

def test_websocket_mask_python_non_multiple_of_4():
    mask = b'\x01\x02\x03\x04'
    data = b'\x10\x20\x30'
    expected_output = b'\x11\x22\x33'
    
    result = _websocket_mask_python(mask, data)
    
    assert result == expected_output
