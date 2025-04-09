# file: lib/ansible/module_utils/connection.py:75-90
# asked: {"lines": [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}
# gained: {"lines": [75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90], "branches": [[78, 79], [78, 83], [80, 81], [80, 82], [85, 86], [85, 90], [87, 88], [87, 89]]}

import pytest
import struct
from unittest.mock import Mock

from ansible.module_utils._text import to_bytes
from ansible.module_utils.connection import recv_data

def test_recv_data_complete_message():
    s = Mock()
    s.recv = Mock(side_effect=[
        struct.pack('!Q', 4),  # header indicating 4 bytes of data
        b'test'  # the actual 4 bytes of data
    ])
    
    result = recv_data(s)
    
    assert result == b'test'

def test_recv_data_incomplete_header():
    s = Mock()
    s.recv = Mock(side_effect=[
        b'\x00\x00\x00\x00',  # incomplete header (4 bytes instead of 8)
        b''  # no more data
    ])
    
    result = recv_data(s)
    
    assert result is None

def test_recv_data_incomplete_message():
    s = Mock()
    s.recv = Mock(side_effect=[
        struct.pack('!Q', 4),  # header indicating 4 bytes of data
        b'te',  # only 2 bytes of data
        b''  # no more data
    ])
    
    result = recv_data(s)
    
    assert result is None

def test_recv_data_empty_socket():
    s = Mock()
    s.recv = Mock(return_value=b'')
    
    result = recv_data(s)
    
    assert result is None
