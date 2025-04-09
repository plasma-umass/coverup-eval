# file: youtube_dl/socks.py:134-136
# asked: {"lines": [136], "branches": []}
# gained: {"lines": [136], "branches": []}

import pytest
from youtube_dl.socks import sockssocket
from youtube_dl.compat import compat_struct_pack

def test_len_and_data():
    data = b'test_data'
    expected_length = len(data)
    expected_result = compat_struct_pack('!B', expected_length) + data
    
    result = sockssocket._len_and_data(data)
    
    assert result == expected_result
